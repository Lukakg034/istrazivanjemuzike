# SEA-B01 — Southeast Asia

Batch label `SEA-B01`. File `research/southeast_asia.csv`. Imported only through `tools/add_records.py`. Staging JSON was deleted after each import that exited 0. One later file was skipped in full because those four titles were already in the file.

## Accepted

8 records, all labelled `SEA-B01`. IDs `SEA-0001`–`SEA-0008`.

| Country | Records |
| --- | ---: |
| Indonesia | 3 |
| Philippines | 1 |
| Vietnam | 1 |
| Cambodia | 1 |
| Thailand | 1 |
| Myanmar | 1 |
| Malaysia | 0 |
| Singapore | 0 |
| Laos | 0 |

Verified 3 (`Bengawan Solo` 1940, `Anak` 1978, `Rayuan Pulau Kelapa` 1944). Partially verified 5. Unverified 0. `piano_arrangement_potential` is `Not assessed` on every row. Every row is Popular.

## What is in the file

Indonesia: `Bengawan Solo` (Gesang, kroncong, 1940), `Begadang` (Rhoma Irama; 1973 and 1975 both appear, so the year is empty), `Rayuan Pulau Kelapa` (Ismail Marzuki, 1944; October versus 15 November, so the day is empty). Philippines: `Anak` (Freddie Aguilar, 1978). Vietnam: `Diễm xưa` (Trịnh Công Sơn, Khánh Ly; 1960 versus 1961, year empty). The genre cell on that row says `Vietnamese popular song`, which is the name used in the imported staging; the taxonomy home for this repertory is `Nhạc trữ tình`. Cambodia: `ចំប៉ាបាត់ដំបង` (Sinn Sisamouth, 1962, Wat Phnom). Thailand: `น้ำตาลาวเวียง` (Suraphol Sombatcharoen; 1953 versus 1954, year empty, composer not named). Myanmar: `အဝေးကချစ်သူ` (Sai Htee Saing, Shan, tied to the 1969 Burma Broadcasting Service session on two biographies that do not both name the title).

## Kept out

`Getaran Jiwa` (P. Ramlee, S. Sudarmaji, 28 May 1960) and `Dahil sa Iyo` (Mike Velarde, film *Bituing Marikit*) were confirmed in searches and not imported here, because both were written for films. Malay film songs of the Singapore studio era and Filipino film kundiman belong with the film file unless a later pass treats them as regional standards.

## Genres added

`Shan popular song` was added to `metadata/genre_taxonomy.md`.

## Sources

Indonesian, Vietnamese, Thai, Burmese and English Wikipedia; ANTARA News; a conference paper on Ismail Marzuki; the composer's site tcs-home.org; a Wat Phnom record note for the Cambodian disc number.

## Gaps

The file is far short of the 80-record aim (72 still to find).

- Malaysia, Singapore and Laos have no rows. No xinyao, no Malay song that was not written for a film, no Lao lam or mor lam.
- Philippines is one song. Kundiman and Pinoy rock are absent.
- No gamelan piece, no jaipongan, no kroncong besides `Bengawan Solo`.
- Thailand is one luk thung song with no composer credit. No mor lam and no Thai classical piphat piece.
- Vietnam is one song with a disputed year. Cambodia is one ballad. Myanmar is one Shan title whose year is inferred.
- `Begadang` has no songwriter credit on the pages used.
- Piano editions were not hunted.
