# SAS-B01 — South Asia

Batch label `SAS-B01`. File `research/south_asia.csv`. Imported only through `tools/add_records.py`. Staging JSON was deleted after each import that exited 0, including a later file whose four rows were skipped as duplicates of rows already in the file.

## Accepted

16 records, all labelled `SAS-B01`. IDs `SAS-0001`–`SAS-0016`.

| Country | Records |
| --- | ---: |
| India | 7 |
| Pakistan | 3 |
| Bangladesh | 3 |
| Nepal | 2 |
| Sri Lanka | 1 |

Verified 6. Partially verified 10. Unverified 0. `piano_arrangement_potential` is `Not assessed` on every row.

## What is in the file

Film songs sit here, as assigned: `आवारा हूँ` (1951), `Chaiyya Chaiyya` (1998), `लग जा गले` (1964), `प्यार किया तो डरना क्या` (5 August 1960). `Allah Hoo` and `دما دم مست قلندر` are qawwali; the second is filed as traditional, not as a Nusrat Fateh Ali Khan composition. Carnatic: `वातापि गणपतिम् भजे` and `ఎందరో మహానుభావులు` (year left empty). Rabindra Sangeet: `একলা চলো রে` (1905) and `আমার সোনার বাংলা` (publication 1905; manuscript lost, melody from Gagan Harkara). Nazrul Geeti: `নতুনের গান` (written February 1928). Nepal: `रेशम फिरिरि` (1969, authorship disputed in one Nepali essay) and `एउटा मान्छेको मायाले कति` (no year on the pages used). Sri Lanka: `දන්නෝ බුදුන්ගේ` from the 1903 nurthi *Sirisangabo*. Baul: Lalon's `জাত গেল জাত গেল বলে`, undated. Pakistan pop: `دل دل پاکستان`, year 1987 against an English Wikipedia infobox that says 1985.

## Genres added

`Pakistani pop`, `Nepali adhunik` and `Sinhala nurthi` were added to `metadata/genre_taxonomy.md`.

## Sources

English, Hindi, Bengali, Urdu and Sinhala Wikipedia; Hamraaz; Tagoreweb and Onushilon for the Tagore song already in the file; BBC Urdu and the Express Tribune for Dil Dil Pakistan; Nazrul Kosh; Annapurna Post; Divaina. A lyrics blog was used only as a second page for the Narayan Gopal credits.

## Gaps

The file is far short of the 80-record aim (64 still to find).

- No Tamil or Telugu film song, no Lollywood song, no bhajan, no bhangra, no Hindustani bandish, no separate ghazal.
- Sri Lanka is one nurthi song. Baila is absent. The tune credit for `දන්නෝ බුදුන්ගේ` rests on one song blog.
- Nepal has no dated Narayan Gopal session beyond the disputed `रेशम फिरिरि` note. `एउटा मान्छेको मायाले कति` has no year.
- Lalon's song is quoted on one biography page only.
- `دما دم مست قلندر` has no agreed author or year. The language field was left empty.
- Piano editions were not hunted.
