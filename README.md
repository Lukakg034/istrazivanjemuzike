# ToneLab — Global Piano Repertoire Research Database

A discovery database of songs, compositions, themes and melodies from musical cultures around the world, collected for later pedagogical review by a professional music educator.

This is a **discovery and documentation** project. Nothing here is a pedagogical judgement: no record is rated for difficulty, suitability or teaching value. `piano_arrangement_potential` is always `Not assessed`.

The full brief is in [`TONE_LAB_PIANO_REPERTOIRE_RESEARCH_MASTER_PROMPT.md`](TONE_LAB_PIANO_REPERTOIRE_RESEARCH_MASTER_PROMPT.md). Current status and the point to resume from are in [`reports/research_progress.md`](reports/research_progress.md).

---

## 1. Folder structure

```text
Istraživanje/
├── TONE_LAB_PIANO_REPERTOIRE_RESEARCH_MASTER_PROMPT.md   research brief
├── README.md                                             this file: methodology and rules
│
├── research/                     primary data, one CSV per region or theme
│   ├── north_america.csv               NAM  USA, Canada, Mexico
│   ├── central_america_caribbean.csv   CAC  Central America, Caribbean islands
│   ├── south_america.csv               SAM  South America incl. Guyana, Suriname
│   ├── europe.csv                      EUR  Europe except the Balkan countries below
│   ├── balkans.csv                     BAL  ex-Yugoslavia, Albania, Kosovo, Bulgaria, Romania, Greece
│   ├── africa.csv                      AFR  all of Africa incl. North Africa and Indian Ocean islands
│   ├── middle_east_central_asia.csv    MEC  Middle East, Turkey, Caucasus, Central Asia
│   ├── south_asia.csv                  SAS  India, Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan, Maldives
│   ├── east_asia.csv                   EAS  Japan, Koreas, China, Taiwan, Hong Kong, Macau, Mongolia
│   ├── southeast_asia.csv              SEA  ASEAN countries and Timor-Leste
│   ├── oceania.csv                     OCE  Australia, New Zealand, Pacific Islands
│   ├── film_tv_animation.csv           FTV  film, TV, animation, anime, musicals and stage
│   ├── video_games.csv                 VGM  video game music
│   ├── classical_historical.csv        CLH  Western art music, opera, ballet, historical melodies
│   └── _staging/                       temporary JSON batches waiting for import
│
├── reports/
│   ├── research_progress.md      batch log and resume point
│   ├── regional_coverage.md      coverage by region and country
│   ├── genre_coverage.md         coverage by genre and tradition
│   ├── research_gaps.md          what still needs exploring
│   ├── database_statistics.md    generated counts and data-quality checks
│   └── batch_notes/              raw notes from each research batch
│
├── metadata/
│   └── genre_taxonomy.md         genre names, controlled vocabularies, naming conventions
│
├── exports/
│   └── master_index.csv          generated: all records merged (UTF-8 with BOM, opens in Excel)
│
└── tools/
    ├── schema.py                 column list and controlled vocabularies
    ├── add_records.py            validated, duplicate-safe import of JSON batches
    └── build_master_index.py     builds exports/master_index.csv and reports/database_statistics.md
```

The regional CSVs are the source of truth. `exports/master_index.csv` and `reports/database_statistics.md` are generated and should not be edited by hand.

---

## 2. Which file does a record belong to?

Each composition has **one** primary record in **one** file. Other associations go into `secondary_associations` and `research_notes`, never into a second record.

Apply these rules in order:

1. **Video game music** (including songs written for games) → `video_games.csv`.
2. **Film, TV, animation, anime and stage music** → `film_tv_animation.csv`. This covers scores, main/opening/ending themes, songs written for a film or show, anime openings and endings, Disney and other animated-film songs, Broadway, West End and international musicals.
   - *Exception:* Indian and other South Asian film songs (Bollywood, Tollywood, Kollywood, Lollywood…) go to `south_asia.csv`, because film song is the mainstream of popular music there. Instrumental background scores from those industries stay in `film_tv_animation.csv`.
   - A pre-existing song that later became famous through a film stays in its regional file, with the film noted in `secondary_associations`.
3. **Western art music** (any country, including composers outside Europe working in the Western classical idiom: Villa-Lobos, Takemitsu, Ginastera…), opera, operetta, ballet, and historical Western melodies before about 1900 → `classical_historical.csv`.
   - Non-Western classical and court traditions (Hindustani, Carnatic, Persian radif, Arabic maqam, Ottoman/Turkish makam, gagaku, Javanese gamelan…) go to their **regional** file.
4. **Everything else** → the regional file for its `country`.

Boundary decisions:

| Country / area | File |
|---|---|
| Mexico | `north_america.csv` |
| Guyana, Suriname, French Guiana | `south_america.csv` |
| Serbia, Croatia, Bosnia and Herzegovina, Montenegro, North Macedonia, Slovenia, Albania, Kosovo, Bulgaria, Romania, Greece | `balkans.csv` |
| Moldova, Cyprus, Hungary, the rest of Europe, Russia, Ukraine, Belarus | `europe.csv` |
| Turkey, Armenia, Georgia, Azerbaijan, Israel, Palestine, the Arab states of Western Asia, Iran, Afghanistan, Central Asia | `middle_east_central_asia.csv` |
| Egypt, the Maghreb, Sudan, Madagascar, Mauritius, Cabo Verde | `africa.csv` |
| Klezmer and Eastern European Jewish music | `europe.csv` (Israeli music goes to `middle_east_central_asia.csv`) |
| Roma music | file of the country it is from, with `Roma music` in `secondary_associations` |

Songs shared across borders (a Balkan melody sung in Turkish, Greek and Serbian versions, for example) get one record, filed under the country with the strongest documented claim or the earliest documented source. List the other countries in `secondary_associations` and explain in `research_notes`. Do not invent an origin when it is disputed: say that it is disputed.

---

## 3. Fields

All CSVs share exactly these columns, in this order. Multi-value fields use ` | ` (space, pipe, space) as the separator.

| Field | Rules |
|---|---|
| `id` | Assigned by `tools/add_records.py`: file prefix plus a four-digit number, e.g. `BAL-0042`. Never reuse or renumber. |
| `title_original` | Title in its original language and script, e.g. `Ушица`, `上を向いて歩こう`, `Ya Rayah`. If the original script is not Latin, give the romanisation in `title_english` or the notes. |
| `title_english` | English translation or romanisation where helpful. Leave empty if the title is already English. Never replace the original title with it. |
| `artist` | Performer most strongly associated with the recording. Use `Traditional` for anonymous folk material with no single reference performer. |
| `composer` | Composer of the music, when identifiable. |
| `songwriter` | Lyricist or songwriting credit; add a role in parentheses, e.g. `Vlado Dijak (lyrics)`. |
| `country` | Country of origin or strongest cultural association of the **composition** (not just the artist's passport). Multi-value only when genuinely shared. |
| `region` | Broader cultural region, e.g. `West Africa`, `Andes`, `Balkans / Southeast Europe`. |
| `language` | Language(s) sung; `Instrumental` if there are no vocals. |
| `genre` | Main genre, using names from `metadata/genre_taxonomy.md`. |
| `subgenre` | More specific style or local form. |
| `musical_tradition` | One of: `Popular`, `Traditional/Folk`, `Jazz`, `Western art music`, `Non-Western art music`, `Sacred/Religious`, `Film/TV/Animation soundtrack`, `Video game music`, `Musical theatre/Stage`. |
| `attribution_type` | One of: `Original composition`, `Traditional/Anonymous`, `Traditional melody, modern arrangement`, `Cover version`, `Adaptation`, `Soundtrack recording`, `Written by others for performer`, `Unknown`. |
| `decade` | Decade of first composition or release, e.g. `1970s`. Use a century for older material (`19th century`), `Traditional (date unknown)`, or leave empty. |
| `year` | Exact four-digit year, **only when verified**. Say in the notes whether it is a composition, publication, premiere or release year. |
| `original_format` | Solo, vocal with band, ensemble, orchestral, electronic, choir, etc. |
| `original_instruments` | Known original instrumentation, multi-value. Leave empty rather than guess. |
| `piano_version_exists` | `Yes` (an original or published piano version is documented), `No` (a source states that none exists), or `Unknown` (default). |
| `piano_arrangement_potential` | Always `Not assessed`. The educator fills this in later. |
| `source_url` | The most reliable source actually consulted. Required. |
| `audio_url` | Official or label/artist-uploaded recording, if one was actually found. Otherwise empty. |
| `additional_source_urls` | Further verification sources, multi-value. |
| `source_language` | Language(s) of the sources used. |
| `verification_status` | `Verified`, `Partially verified` or `Unverified` (see section 4). |
| `secondary_associations` | Other genres, countries, films, movements or categories, multi-value. |
| `research_batch` | Batch label, e.g. `EUR-B03`. Filled in automatically on import. |
| `research_notes` | Facts that clarify attribution, dates, versions or uncertainty. No opinions on teaching value. |

---

## 4. Sources and verification

### Verification levels

- **Verified**: title, performer/composer attribution, country and date are confirmed by an authoritative source (official artist, label or composer site; Discogs or MusicBrainz release data; a national archive or cultural institution; an encyclopedia entry with citations; film or game credits), **and** at least one independent source agrees.
- **Partially verified**: the composition and its main attribution are confirmed by at least one reliable source, but some metadata (date, composer, origin) rests on a single source or is uncertain.
- **Unverified**: the composition was found, but the metadata could not be checked against a reliable source. Use sparingly, and explain why in the notes.

### Rules that are never broken

- Every URL in the database must have been **actually returned by a search or opened during research**. Never type a URL from memory, never construct one from a pattern (for example by guessing a Discogs ID or a YouTube video ID), and never "fix" a broken link by guessing.
- Never fabricate titles, artists, composers, countries, dates, genres or links. A plausible-sounding result is not a verified result.
- Automatically generated playlists and unverified user uploads are discovery aids only. They are never evidence for authorship or dates.
- Do not attribute traditional music to the modern performer who popularised it. Use `attribution_type` to make the distinction.
- Keep apart: artist country vs. song origin, recording year vs. composition year, release date vs. traditional origin, performer vs. composer, genre vs. region.
- Do not reproduce lyrics or sheet music. Do not download copyrighted material.

### Preferred sources

Official artist, composer and label sites; Discogs; MusicBrainz; AllMusic; national and regional music encyclopedias and archives; cultural institutions; film and game credit databases (IMDb, VGMdb); reputable music journalism; Wikipedia in the **local language** as well as English, preferably checked against a second source; official streaming pages for discovery.

---

## 5. Research workflow

Research is done in batches, each covering one region, country group or theme. For each batch:

1. Identify the countries and local scenes, then search in English **and** in the local language(s), using local genre terms and original titles.
2. Cover internationally known material, then deliberately go further: regional and independent artists, traditional and folk repertoire, older recordings, contemporary local scenes, and styles rarely represented in European music education.
3. Prefer breadth over depth: many artists, genres, decades and communities rather than many songs by one famous artist. As a rule of thumb, no more than three records per artist in one batch.
4. Write the records to a JSON file in `research/_staging/`, a list of objects whose keys are the field names above (omit `id`):

   ```json
   [
     {
       "title_original": "Selma",
       "artist": "Bijelo Dugme",
       "composer": "Goran Bregović",
       "songwriter": "Vlado Dijak (lyrics)",
       "country": "Bosnia and Herzegovina",
       "region": "Balkans / Southeast Europe",
       "language": "Serbo-Croatian",
       "genre": "Rock",
       "musical_tradition": "Popular",
       "attribution_type": "Original composition",
       "decade": "1970s",
       "year": "1974",
       "source_url": "https://en.wikipedia.org/wiki/Kad_bi%27_bio_bijelo_dugme",
       "additional_source_urls": ["https://muzikalnastranica.com.hr/dugme/kad-bi-bio.html"],
       "verification_status": "Verified",
       "research_notes": "..."
     }
   ]
   ```

5. Import it:

   ```powershell
   python tools/add_records.py research/balkans.csv research/_staging/bal_b01.json --batch BAL-B01
   ```

   The script validates every record, assigns IDs, skips duplicates already present in **any** research file, and reports anything rejected. Fix rejected records and import them again (accepted ones are not imported twice). Add `--dry-run` to validate without writing. Delete the staging file after a successful import.

6. Write a short batch note in `reports/batch_notes/` covering the countries and genres covered, record counts by verification status, the main sources, and what still needs exploring.
7. After all the batches in a round are done, rebuild the index and update the reports:

   ```powershell
   python tools/build_master_index.py
   ```

Never mark a country or region as "fully researched" because a handful of popular songs has been collected.

---

## 6. Opening the data

- **Web explorer:** open [`docs/index.html`](docs/index.html) (GitHub Pages, or double-click the file). Search, filter by collection, country, tradition, decade, genre and verification. Rebuild `docs/data.js` with `python tools/build_master_index.py` after new imports.
- **Excel:** open `exports/master_index.csv` directly (it has a UTF-8 BOM, so Cyrillic, Arabic, CJK and other scripts display correctly). The regional CSVs are plain UTF-8: import them with *Data → From Text/CSV* and choose *65001: Unicode (UTF-8)*.
- **Google Sheets / LibreOffice:** import any CSV as UTF-8, comma-separated.
- **Python:** `csv.DictReader(open(path, encoding="utf-8-sig"))`.

---

## 7. Resuming the research

1. Read `reports/research_progress.md` (the latest batch and the next steps) and `reports/research_gaps.md`.
2. Pick an underrepresented region or genre from `reports/regional_coverage.md` and `reports/genre_coverage.md`.
3. Follow the workflow in section 5, using the next free batch number for that file (e.g. `AFR-B04`).
