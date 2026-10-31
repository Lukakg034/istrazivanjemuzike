"""Shared schema for the ToneLab repertoire research database.

Every research CSV uses exactly these columns in this order. Controlled
vocabularies are defined here so that the import and index scripts agree.
"""

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = ROOT / "research"
STAGING_DIR = RESEARCH_DIR / "_staging"
REPORTS_DIR = ROOT / "reports"
EXPORTS_DIR = ROOT / "exports"

COLUMNS = [
    "id",
    "title_original",
    "title_english",
    "artist",
    "composer",
    "songwriter",
    "country",
    "region",
    "language",
    "genre",
    "subgenre",
    "musical_tradition",
    "attribution_type",
    "decade",
    "year",
    "original_format",
    "original_instruments",
    "musical_key",
    "time_signature",
    "chord_progression",
    "piano_version_exists",
    "piano_arrangement_potential",
    "source_url",
    "audio_url",
    "additional_source_urls",
    "source_language",
    "verification_status",
    "secondary_associations",
    "research_batch",
    "research_notes",
]

FILE_PREFIXES = {
    "north_america.csv": "NAM",
    "central_america_caribbean.csv": "CAC",
    "south_america.csv": "SAM",
    "europe.csv": "EUR",
    "balkans.csv": "BAL",
    "africa.csv": "AFR",
    "middle_east_central_asia.csv": "MEC",
    "south_asia.csv": "SAS",
    "east_asia.csv": "EAS",
    "southeast_asia.csv": "SEA",
    "oceania.csv": "OCE",
    "film_tv_animation.csv": "FTV",
    "video_games.csv": "VGM",
    "classical_historical.csv": "CLH",
}

FILE_LABELS = {
    "north_america.csv": "North America",
    "central_america_caribbean.csv": "Central America & Caribbean",
    "south_america.csv": "South America",
    "europe.csv": "Europe",
    "balkans.csv": "Balkans",
    "africa.csv": "Africa",
    "middle_east_central_asia.csv": "Middle East & Central Asia",
    "south_asia.csv": "South Asia",
    "east_asia.csv": "East Asia",
    "southeast_asia.csv": "Southeast Asia",
    "oceania.csv": "Oceania",
    "film_tv_animation.csv": "Film, TV & animation",
    "video_games.csv": "Video games",
    "classical_historical.csv": "Western art music",
}

REQUIRED_FIELDS = [
    "title_original",
    "country",
    "musical_tradition",
    "attribution_type",
    "source_url",
    "verification_status",
]

VERIFICATION_STATUS = ["Verified", "Partially verified", "Unverified"]

PIANO_VERSION_EXISTS = ["Yes", "No", "Unknown"]

PIANO_ARRANGEMENT_POTENTIAL = "Not assessed"

MUSICAL_TRADITION = [
    "Popular",
    "Traditional/Folk",
    "Jazz",
    "Western art music",
    "Non-Western art music",
    "Sacred/Religious",
    "Film/TV/Animation soundtrack",
    "Video game music",
    "Musical theatre/Stage",
]

ATTRIBUTION_TYPE = [
    "Original composition",
    "Traditional/Anonymous",
    "Traditional melody, modern arrangement",
    "Cover version",
    "Adaptation",
    "Soundtrack recording",
    "Written by others for performer",
    "Unknown",
]

MULTI_VALUE_SEPARATOR = " | "

MULTI_VALUE_FIELDS = {
    "country",
    "original_instruments",
    "additional_source_urls",
    "secondary_associations",
    "language",
}

URL_FIELDS = {"source_url", "audio_url"}

ID_PATTERN = re.compile(r"^([A-Z]{3})-(\d{4,})$")
YEAR_PATTERN = re.compile(r"^\d{4}$")


def normalise_key(text: str) -> str:
    """Return a comparison key that ignores case, diacritics and punctuation."""
    if not text:
        return ""
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    stripped = stripped.casefold()
    return re.sub(r"[\W_]+", "", stripped)


def duplicate_key(record: dict) -> str:
    """Records with the same title and the same artist (or composer) are duplicates."""
    title = normalise_key(record.get("title_original", ""))
    who = normalise_key(record.get("artist", "")) or normalise_key(record.get("composer", ""))
    return f"{title}||{who}"


def match_vocabulary(value: str, vocabulary: list[str]) -> str | None:
    """Case-insensitive lookup in a controlled vocabulary."""
    wanted = value.strip().casefold()
    for option in vocabulary:
        if option.casefold() == wanted:
            return option
    return None
