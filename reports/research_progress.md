# Research progress

**Status:** Round 1 paused in a consistent state. Resume from [`research_gaps.md`](research_gaps.md).

**Updated:** 31 October 2026  
**Total records:** 847  
**Verification:** 352 Verified · 495 Partially verified · 0 Unverified  
**Countries / cultural areas in the `country` field:** 102  
**Distinct genres:** 183  
**Data-quality issues flagged by the index script:** none  

Rebuild after every import:

```powershell
python tools/build_master_index.py
```

---

## What happened

1. Folder, schema, import/index tools, README and taxonomy were created.
2. A first wave of researchers hit a model-usage limit. Three of them had already written Balkans rock, UK/Ireland, and Cuban danzón.
3. Research continued with sourced seed records for every empty file.
4. A second wave on Grok finished several files:
   - [Balkans/Europe/MECA](a3455129-a49a-4642-9c29-01a58d7f12ea)
   - [North America](47f13b22-0c6c-4805-aa60-6fecbbce0f9c)
   - [Africa](bd54a3a1-497e-4456-9c46-55494e145278)
   - [Film/games/classical/Oceania](39fd1c09-6ae1-4710-aa53-6a6095fbfaf5)
5. Leftover staging was imported (`SAM-B01`, then four South Asia and four Southeast Asia titles).
6. Five artist-string near-duplicates were dropped (`NAM-0026`, `AFR-0007`, `AFR-0020`, `EAS-0007`, `EAS-0030`). Title collisions are now empty.
7. [South America](c696e8a6-b549-4691-a6e7-f241884f34c6) expanded `south_america.csv` to 121 (all twelve countries). Staging was already empty.
8. [East/South/Southeast Asia](6820e072-e348-4023-952c-5f2e0f24da85) added four South Asia and two Southeast Asia rows. East Asia stayed at 78 after the earlier near-duplicate drop.

---

## Records per file

| File | Records | Verified | Partial | Last batch |
|---|---:|---:|---:|---|
| `africa.csv` | 149 | 20 | 129 | AFR-B01 |
| `oceania.csv` | 122 | 4 | 118 | OCE-B01 |
| `south_america.csv` | 121 | 54 | 67 | SAM-B01 |
| `north_america.csv` | 120 | 100 | 20 | NAM-B01 |
| `balkans.csv` | 87 | 18 | 69 | BAL-B02 |
| `east_asia.csv` | 78 | 51 | 27 | EAS-B01 |
| `europe.csv` | 55 | 45 | 10 | EUR-B03 |
| `film_tv_animation.csv` | 32 | 17 | 15 | FTV-B01 |
| `central_america_caribbean.csv` | 23 | 15 | 8 | CAC-B02 |
| `middle_east_central_asia.csv` | 15 | 7 | 8 | MEC-B01 |
| `south_asia.csv` | 16 | 6 | 10 | SAS-B01 |
| `classical_historical.csv` | 11 | 7 | 4 | CLH-B01 |
| `video_games.csv` | 10 | 5 | 5 | VGM-B01 |
| `southeast_asia.csv` | 8 | 3 | 5 | SEA-B01 |

Oceania and Africa have a high share of Partially verified rows. Treat those as discovery leads, not as closed documentation.

---

## Batch notes on disk

| Note | File |
|---|---|
| `reports/batch_notes/NAM-B01.md` | United States, Canada, Mexico |
| `reports/batch_notes/AFR-B01.md` | Africa |
| `reports/batch_notes/OCE-B01.md` | Oceania |
| `reports/batch_notes/CAC-B02.md` | Caribbean / Central America beyond Cuba |
| `reports/batch_notes/CLH-B01.md` | Western art music |
| `reports/batch_notes/VGM-B01.md` | Video games |
| `reports/batch_notes/FTV-B01.md` | Film / TV / stage |
| `reports/batch_notes/SAM-B01.md` | South America (all 12 countries) |
| `reports/batch_notes/EAS-B01.md` | East Asia |
| `reports/batch_notes/EUR-B03.md` | Continental Europe |
| `reports/batch_notes/MEC-B01.md` | Middle East / Caucasus seed |
| `reports/batch_notes/BAL-B02.md` | Balkans gap-fill |
| `reports/batch_notes/SAS-B01.md` | South Asia |
| `reports/batch_notes/SEA-B01.md` | Southeast Asia |

---

## Next batch numbers

Work **thin files and empty countries** first. Do not add more New Zealand pop, US chart rock, Brazilian MPB, or ex-Yu new wave until Southeast Asia, South Asia and Central Asia have real coverage.

| Next batch | File | Why |
|---|---|---|
| SEA-B02 | `southeast_asia.csv` | 8 records; Malaysia, Singapore and Laos still empty |
| SAS-B02 | `south_asia.csv` | 16 records; no Maldives or Bhutan; no Tamil/Telugu film |
| MEC-B02 | `middle_east_central_asia.csv` | no Gulf, Palestine, Armenia, Central Asia |
| SAM-B02 | `south_america.csv` | Bolivia 1, Guyana 1, Suriname 2; sampled cueca/huayno/vallenato — not more Brazilian MPB |
| CAC-B03 | `central_america_caribbean.csv` | no Puerto Rico, most of Central America, French Antilles |
| EUR-B04 | `europe.csv` | no Baltics, Finland, Denmark, Iceland, Slovakia, Switzerland |
| BAL-B03 | `balkans.csv` | Albania/Montenegro still thin; more folk, less rock |
| FTV-B02 / VGM-B02 / CLH-B02 | thematic files | still far below the brief |
| AFR-B02 | `africa.csv` | Maghreb, Sahel and Indian Ocean still thin relative to DRC/SA/Ethiopia |
| OCE-B02 | `oceania.csv` | Pacific Islands almost empty; NZ is over-represented |

---

## Known data issues (not fatal)

- **51 rows have an empty `genre`.** Fill only from a source, do not guess.
- `Aloha ʻOe` is in `north_america.csv` (Hawaiʻi / United States), which matches the README.
- `piano_arrangement_potential` is `Not assessed` on every row.

---

## Sources used across Round 1

Wikipedia (English and local-language), Discogs, MusicBrainz, VGMdb, DAHR, Library of Congress, UNESCO ICH, national encyclopedias and charts, official artist/label pages, ECAD, Afrodisc, Carnatica.net, NASA Voyager list. Every stored URL was returned by a search or a fetch during research.
