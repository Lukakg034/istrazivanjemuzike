# EAS-B01 — East Asia

Batch label `EAS-B01`. File `research/east_asia.csv`. Imported only through `tools/add_records.py`. Staging JSON was deleted after each successful import.

## Accepted

80 records in the file, all labelled `EAS-B01`. IDs `EAS-0001`–`EAS-0080`. Five rows (`EAS-0001`–`EAS-0005`) were already in the file when this batch continued; the rest were accepted in six imports (29, 15, 6, 8, 12, 5). The importer skipped three exact duplicates of songs already present (`さくらさくら`, `아리랑`, `茉莉花`).

Two near-duplicates were later dropped because the artist string differed: `EAS-0007` (`上を向いて歩こう`, `坂本九`) and `EAS-0030` (`月亮代表我的心`, `鄧麗君`). Kept `EAS-0001` and `EAS-0005`. File now **78**.

## Countries

| Country | Records |
| --- | ---: |
| Japan | 32 |
| China | 14 |
| South Korea | 13 |
| Taiwan | 7 |
| Hong Kong | 7 |
| Mongolia | 4 |
| North Korea | 1 |

## Verification and tradition

Verified 51. Partially verified 27. Unverified 0. `piano_arrangement_potential` is `Not assessed` on every row. `piano_version_exists` is Unknown on every remaining row.

Popular 46. Traditional/Folk 16. Non-Western art music 15. Jazz 1.

## What was kept out

Anime, game and film scores written for the screen were not entered. `동백아가씨` (Lee Mi-ja, 1964) is a film theme and was left for the film file. `天才與白痴` was written as the theme of the 1975 Hui film and was left out. Pre-existing songs later used in film or television (for example `First Love`, `ひこうき雲`, `Endless Rain`, `我願意`) stay here, with the later use in `secondary_associations`.

Western-idiom art songs were not entered. Court and classical pieces that are not Western art music were entered as Non-Western art music: gagaku (`越天楽`), koto (`春の海`, `六段の調`), shakuhachi honkyoku (`鶴の巣籠`), pansori (`춘향가`, `심청가`), gayageum sanjo, guqin (`广陵散`, `流水`), pipa (`十面埋伏`), guzheng (`渔舟唱晚`).

## Sources

Japanese, Korean and Chinese Wikipedia, often paired with a label, official artist page, encyclopedia or archive: Columbia, Universal, Oricon, Tower, Kotobank, Agency for Cultural Affairs, Okinawa prefecture, Encyclopedia of Korean Culture, National Gugak Center, Grand Culture, NDL, UNESCO, National Museum of Taiwan History, Teng Yu-hsien digital archive, BBC Chinese, Golden Melody coverage inside Wikipedia album pages, Sadao Watanabe’s site, Shankar is not in this file. Years were left blank where sources disagreed (`돌아와요 부산항에`, `휘파람`, `广陵散`, `康定情歌`, `渔舟唱晚`).

## Gaps

- Japan is heavy relative to the rest of the region. Ainu music is one named upopo (`チュㇷ゚カ ワ`), not a wider repertory. Ryukyu is two songs. Jazz is one album title track, and its composer credit was not on the pages consulted.
- North Korea is a single popular song (`휘파람`), with the release year left empty.
- Mongolia is two named practices (`Уртын дуу`, `Хөөмий`, `Морин хуур`) plus one band song. A single notated long-song melody was not pinned down.
- Cantopop and Mandopop after 2005, Taiwan campus folk beyond `橄欖樹`, and Okinawan classical (utakata / koten) are thin.
- `海闊天空` is only partially verified. `康定情歌` authorship is disputed and was not assigned.
- No piano editions were hunted. `piano_version_exists` is Unknown except where a source already stated a piano publication.
