"""Fill empty audio_url fields from a JSON list of {id, audio_url}.

Usage:
    python tools/set_audio_urls.py research/_staging/audio_urls.json
"""

import csv
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schema import COLUMNS, RESEARCH_DIR  # noqa: E402

ALLOWED_HOSTS = {
    "www.youtube.com",
    "youtube.com",
    "youtu.be",
    "m.youtube.com",
    "music.youtube.com",
    "open.spotify.com",
    "soundcloud.com",
    "www.soundcloud.com",
    "vimeo.com",
    "www.vimeo.com",
    "dailymotion.com",
    "www.dailymotion.com",
    "archive.org",
}


def normalise_url(url: str) -> str:
    url = (url or "").strip()
    if not url.startswith(("http://", "https://")):
        raise ValueError(f"not http(s): {url}")
    host = urlparse(url).netloc.lower()
    if host not in ALLOWED_HOSTS:
        raise ValueError(f"host not allowed: {host}")
    if host in {"www.youtube.com", "youtube.com", "m.youtube.com", "music.youtube.com"}:
        if "watch?v=" not in url and "/embed/" not in url and "/shorts/" not in url:
            raise ValueError(f"youtube URL is not a video: {url}")
    if host == "youtu.be" and urlparse(url).path.strip("/") == "":
        raise ValueError(f"empty youtu.be path: {url}")
    return url


def load_updates(path: Path) -> dict[str, str]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(payload, dict) and "records" in payload:
        payload = payload["records"]
    updates = {}
    for item in payload:
        record_id = item["id"].strip()
        updates[record_id] = normalise_url(item["audio_url"])
    return updates


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python tools/set_audio_urls.py <json>")
    updates = {}
    skipped = []
    for arg in sys.argv[1:]:
        path = Path(arg)
        for record_id, url in load_updates(path).items():
            updates[record_id] = url

    filled = 0
    already = 0
    missing = 0
    for csv_path in sorted(RESEARCH_DIR.glob("*.csv")):
        rows = list(csv.DictReader(csv_path.open(encoding="utf-8-sig", newline="")))
        changed = False
        for row in rows:
            url = updates.pop(row["id"], None)
            if not url:
                continue
            if row.get("audio_url"):
                already += 1
                continue
            row["audio_url"] = url
            filled += 1
            changed = True
        if changed:
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
                writer.writeheader()
                writer.writerows({column: row.get(column, "") for column in COLUMNS} for row in rows)
    missing = len(updates)
    print(f"filled {filled}, already had audio {already}, unknown ids {missing}")
    for record_id in sorted(updates):
        print(" unknown", record_id)


if __name__ == "__main__":
    main()
