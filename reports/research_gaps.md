# Research gaps

Round 1 is at **847 sourced records**. The collection is internationally broader than at the seed stage, but several regions the brief named as essential are still almost empty.

## Do this next

1. **Southeast Asia** (`SEA-B02`). Malaysia/Singapore (non-film P. Ramlee or xinyao), Laos, named gamelan pieces, more dangdut and OPM, nhạc vàng beyond one Trịnh title. Myanmar now has one Shan title.
2. **South Asia** (`SAS-B02`). Tamil/Telugu film, ghazal, qawwali beyond two titles, Hindustani bandish, baila, Bhutan, Maldives. Sri Lanka and a third Bangladesh title are now in. Lata is at two songs.
3. **Central Asia and the rest of MEC** (`MEC-B02`). Kazakhstan/Kyrgyzstan/Uzbekistan/Tajikistan/Turkmenistan; Armenia; Palestine, Syria, Iraq, Yemen, Gulf; Persian classical; Turkish makam and arabesk.
4. **Caribbean and Central America beyond Cuba** (`CAC-B03`). Puerto Rico (salsa, bomba, plena), merengue/bachata, calypso/soca, Garifuna, French Antilles zouk/biguine.
5. **Europe north and east** (`EUR-B04`). Baltics, Finland, Denmark, Iceland, Slovakia, Switzerland; more than one song each for Poland, Czechia, Hungary, Ukraine, Russia.
6. **Balkan folk** (`BAL-B03`). A titled Albanian iso-polyphonic song if a source names one; Montenegro; klapa; ganga/ojkanje; more sevdah; Guča brass *tunes*; Romanian taraf/fanfare.
7. **Thematic files.** Anime OP/ED, TV themes from more countries, Broadway/West End, non-Japanese games, opera/ballet/minimalism. Confirmed and held for FTV: *Getaran Jiwa*, *Dahil sa Iyo*.
8. **South America deepen** (`SAM-B02`) only after the holes above: Bolivia, Guyana, Suriname, a second huayno/vallenato/cueca. Do not add more Brazilian MPB.

## Quality gaps (not just missing countries)

- **Oceania:** 118/122 Partially verified, and most records are New Zealand. Next Oceania work should be Pacific Islands and Aboriginal/Māori traditional material, not more Flying Nun singles.
- **Africa:** 129/149 Partially verified. DRC, South Africa and Ethiopia are far ahead of West Africa and the Maghreb.
- **Empty `genre` on 51 rows.**
- **South America** now has all twelve countries, but Bolivia and Guyana are still one song each. Paraguay is guarania-heavy.

Artist-string near-duplicates of *La Bamba*, *Zombie*, *Inta Omri*, *Ue o muite arukō* and *The Moon Represents My Heart* were dropped. Keep the remaining IDs (`NAM-0005`, `AFR-0001`, `AFR-0005`, `EAS-0001`, `EAS-0005`).

## Attribution reminders already in the notes

Misirlou (shared Eastern Mediterranean). No Woman, No Cry (Ford credit). Cielito lindo (older Andalusian verses). Sarı gəlin (disputed origin; one record under Azerbaijan). Inta Omri (1964 vs 1965). Chega de Saudade (Cardoso recorded first).

## How to continue

`README.md` section 5: JSON staging of 20–30 records, `python tools/add_records.py …`, delete staging, write `reports/batch_notes/<BATCH>.md`, then `python tools/build_master_index.py`. Never mark a country done.
