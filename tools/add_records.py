"""Append research records from a JSON staging file to a research CSV.

Usage:
    python tools/add_records.py research/europe.csv research/_staging/eur_b01.json --batch EUR-B01

The JSON file must contain a list of objects whose keys are column names
(see README.md). Do not supply "id"; it is assigned automatically.

The script:
  * validates required fields and controlled vocabularies,
  * forces piano_arrangement_potential to "Not assessed",
  * skips records that duplicate an existing record in ANY research CSV,
  * appends accepted records under a file lock, so several researchers can
    write to the same CSV safely,
  * prints a summary of accepted, skipped and rejected records.
"""

import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schema import (  # noqa: E402
    ATTRIBUTION_TYPE,
    COLUMNS,
    FILE_PREFIXES,
    ID_PATTERN,
    MULTI_VALUE_FIELDS,
    MULTI_VALUE_SEPARATOR,
    MUSICAL_TRADITION,
    PIANO_ARRANGEMENT_POTENTIAL,
    PIANO_VERSION_EXISTS,
    REQUIRED_FIELDS,
    RESEARCH_DIR,
    URL_FIELDS,
    VERIFICATION_STATUS,
    YEAR_PATTERN,
    duplicate_key,
    match_vocabulary,
)

LOCK_TIMEOUT_SECONDS = 120
STALE_LOCK_SECONDS = 300


def acquire_lock(lock_path: Path) -> None:
    deadline = time.time() + LOCK_TIMEOUT_SECONDS
    while True:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            return
        except FileExistsError:
            try:
                if time.time() - lock_path.stat().st_mtime > STALE_LOCK_SECONDS:
                    lock_path.unlink(missing_ok=True)
                    continue
            except FileNotFoundError:
                continue
            if time.time() > deadline:
                raise SystemExit(f"Could not acquire lock {lock_path}; another import is running.")
            time.sleep(0.5)


def release_lock(lock_path: Path) -> None:
    lock_path.unlink(missing_ok=True)


def read_csv(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    for attempt in range(5):
        try:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                return list(csv.DictReader(handle))
        except (OSError, csv.Error):
            time.sleep(0.5 * (attempt + 1))
    raise SystemExit(f"Could not read {path}")


def existing_keys() -> dict[str, str]:
    """Map duplicate keys to record IDs across every research CSV."""
    keys = {}
    for csv_name in FILE_PREFIXES:
        for row in read_csv(RESEARCH_DIR / csv_name):
            key = duplicate_key(row)
            if key and not key.startswith("||"):
                keys.setdefault(key, row.get("id", "?"))
    return keys


def next_id_number(rows: list[dict], prefix: str) -> int:
    highest = 0
    for row in rows:
        match = ID_PATTERN.match(row.get("id", ""))
        if match and match.group(1) == prefix:
            highest = max(highest, int(match.group(2)))
    return highest + 1


def clean_value(field: str, value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        parts = [str(item).strip() for item in value if str(item).strip()]
        return MULTI_VALUE_SEPARATOR.join(parts)
    text = str(value).strip()
    if field in MULTI_VALUE_FIELDS:
        parts = [part.strip() for part in text.split("|") if part.strip()]
        text = MULTI_VALUE_SEPARATOR.join(parts)
    return " ".join(text.split()) if field == "research_notes" else text


def validate(record: dict) -> tuple[dict | None, list[str]]:
    problems = []
    unknown = sorted(set(record) - set(COLUMNS))
    if unknown:
        problems.append(f"unknown fields {unknown}")
    if "id" in record and record["id"]:
        problems.append("do not supply 'id'; it is assigned automatically")

    row = {column: clean_value(column, record.get(column)) for column in COLUMNS}
    row["id"] = ""

    for field in REQUIRED_FIELDS:
        if not row[field]:
            problems.append(f"missing {field}")
    if not row["artist"] and not row["composer"]:
        problems.append("artist or composer is required (use 'Traditional' for anonymous music)")

    checks = [
        ("verification_status", VERIFICATION_STATUS),
        ("musical_tradition", MUSICAL_TRADITION),
        ("attribution_type", ATTRIBUTION_TYPE),
    ]
    for field, vocabulary in checks:
        if row[field]:
            matched = match_vocabulary(row[field], vocabulary)
            if matched is None:
                problems.append(f"{field}={row[field]!r} not in {vocabulary}")
            else:
                row[field] = matched

    version = match_vocabulary(row["piano_version_exists"] or "Unknown", PIANO_VERSION_EXISTS)
    if version is None:
        problems.append(f"piano_version_exists={row['piano_version_exists']!r} not in {PIANO_VERSION_EXISTS}")
    else:
        row["piano_version_exists"] = version
    row["piano_arrangement_potential"] = PIANO_ARRANGEMENT_POTENTIAL

    for field in URL_FIELDS:
        if row[field] and not row[field].startswith(("http://", "https://")):
            problems.append(f"{field} is not an http(s) URL")
    for url in row["additional_source_urls"].split(MULTI_VALUE_SEPARATOR):
        if url and not url.startswith(("http://", "https://")):
            problems.append(f"additional_source_urls contains a non-URL value {url!r}")

    if row["year"] and not YEAR_PATTERN.match(row["year"]):
        problems.append(f"year={row['year']!r} must be a four-digit year or empty")

    return (None, problems) if problems else (row, [])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv_path", help="Target research CSV, e.g. research/europe.csv")
    parser.add_argument("json_path", help="JSON file containing a list of record objects")
    parser.add_argument("--batch", required=True, help="Research batch label, e.g. EUR-B01")
    parser.add_argument("--dry-run", action="store_true", help="Validate only; do not write")
    args = parser.parse_args()

    csv_path = Path(args.csv_path).resolve()
    if csv_path.name not in FILE_PREFIXES or csv_path.parent != RESEARCH_DIR.resolve():
        raise SystemExit(f"Target must be one of research/{list(FILE_PREFIXES)}")
    prefix = FILE_PREFIXES[csv_path.name]

    with open(args.json_path, encoding="utf-8-sig") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise SystemExit("JSON root must be a list of record objects")

    lock_path = csv_path.with_suffix(".csv.lock")
    acquire_lock(lock_path)
    try:
        rows = read_csv(csv_path)
        seen = existing_keys()
        number = next_id_number(rows, prefix)
        accepted, skipped, rejected = [], [], []

        for index, record in enumerate(records, start=1):
            label = f"#{index} {record.get('title_original', '?')!r}"
            if not isinstance(record, dict):
                rejected.append((label, ["record is not an object"]))
                continue
            row, problems = validate(record)
            if problems:
                rejected.append((label, problems))
                continue
            key = duplicate_key(row)
            if key in seen:
                skipped.append((label, seen[key]))
                continue
            row["id"] = f"{prefix}-{number:04d}"
            row["research_batch"] = row["research_batch"] or args.batch
            number += 1
            seen[key] = row["id"]
            accepted.append(row)

        if accepted and not args.dry_run:
            write_header = not csv_path.exists() or csv_path.stat().st_size == 0
            with csv_path.open("a", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
                if write_header:
                    writer.writeheader()
                writer.writerows(accepted)
    finally:
        release_lock(lock_path)

    mode = "DRY RUN - nothing written. " if args.dry_run else ""
    print(f"{mode}{csv_path.name}: {len(accepted)} accepted, {len(skipped)} duplicates skipped, {len(rejected)} rejected")
    if accepted:
        print(f"  IDs {accepted[0]['id']} .. {accepted[-1]['id']}")
    for label, existing in skipped:
        print(f"  DUPLICATE {label} already exists as {existing}")
    for label, problems in rejected:
        print(f"  REJECTED {label}: {'; '.join(problems)}")
    if rejected:
        sys.exit(2)


if __name__ == "__main__":
    main()
