# Genre taxonomy and naming conventions

This file keeps `genre`, `subgenre` and `musical_tradition` consistent across all research files.

It is a working reference, not a closed list. When a style is missing, add it under the right family, in the local name used by the people who make the music, and record the addition in `reports/research_progress.md`.

---

## 1. How the three classification fields work together

| Field | Question it answers | Example |
|---|---|---|
| `musical_tradition` | What broad sphere of music is this? (controlled list) | `Traditional/Folk` |
| `genre` | Which named genre or form? | `Sevdalinka` |
| `subgenre` | Which specific variety, scene or local form? | `Urban love song (Mostar)` |

Conventions:

- When a local form is itself the recognised genre name, use it as `genre` (`Fado`, `Tango`, `Sevdalinka`, `Highlife`, `Dangdut`, `Rebetiko`, `Qawwali`, `Mbalax`). Do not file it under a generic Western label like "Folk" or "World music".
- **Never use `World music`** as a genre. It is a marketing label, not a style.
- Use the established spelling in the Latin alphabet, keeping diacritics: `Lăutărească`, `Forró`, `Laïko`, `Starogradska muzika`, `Luk thung`, `Mor lam`.
- Genre describes style, not place. `Rock` from Serbia is `genre = Rock`, `subgenre = Yugoslav rock` or `Yugoslav new wave`, `country = Serbia`.
- Fusions: put the dominant style in `genre`, the fusion in `subgenre`, and the other styles in `secondary_associations`.

---

## 2. `musical_tradition` (controlled)

| Value | Use for |
|---|---|
| `Popular` | Commercially recorded or broadcast popular music of any era and country, including popular music built on folk idioms (turbo-folk, dangdut, bachata). |
| `Traditional/Folk` | Traditional, folk, oral and community music, including modern performances of traditional repertoire. |
| `Jazz` | Jazz and its direct offshoots (swing, bebop, Ethio-jazz, South African jazz, Latin jazz). |
| `Western art music` | Western classical, opera, ballet, contemporary classical, minimalism, neoclassical. |
| `Non-Western art music` | Classical and court traditions outside the Western canon: Hindustani, Carnatic, Persian radif, Arabic classical/maqam, Turkish makam, gagaku, Javanese and Balinese gamelan, Korean jeongak, Chinese literati repertoire. |
| `Sacred/Religious` | Liturgical and devotional music when that is its primary identity (gospel can be either `Popular` or this; choose the better fit and say so in the notes). |
| `Film/TV/Animation soundtrack` | Music written for film, television or animation. |
| `Video game music` | Music written for games. |
| `Musical theatre/Stage` | Musicals, revues, zarzuela and other stage works outside opera. |

---

## 3. `attribution_type` (controlled)

| Value | Use for |
|---|---|
| `Original composition` | Written by an identifiable composer or songwriter, recorded by them or by the reference performer. |
| `Traditional/Anonymous` | No known author; transmitted orally or in folk collections. |
| `Traditional melody, modern arrangement` | Traditional melody or text in a well-known modern arrangement or setting (record the arranger in `composer` or the notes). |
| `Cover version` | The record describes a cover; the original must be named in the notes. Prefer recording the original instead. |
| `Adaptation` | A new text, translation or substantial reworking of an existing piece (e.g. a Yugoslav cover with new lyrics of an Italian song). |
| `Soundtrack recording` | A cue or theme credited as part of a score, where the "work" is the soundtrack piece. |
| `Written by others for performer` | Strongly associated with a performer who did not write it (most Motown, K-pop, turbo-folk and chanson hits). |
| `Unknown` | Authorship could not be established. |

---

## 4. Genre families

Canonical `genre` names are in **bold**. Examples of `subgenre` values follow each one.

### Popular — Anglo-American roots and derivatives
- **Blues**: Delta blues, Chicago blues, Piedmont blues, Texas blues, Desert blues (Tuareg, use in Africa)
- **Ragtime**
- **Boogie-woogie**
- **Gospel**: Traditional gospel, Contemporary gospel, Spiritual
- **Country**: Honky-tonk, Bluegrass, Outlaw country, Western swing, Country pop
- **Folk**: American folk revival, British folk revival, Singer-songwriter, Protest song
- **Music hall**: London music hall, Victorian and Edwardian popular song
- **Skiffle**
- **Rock and roll**
- **Rock**: Classic rock, Hard rock, Progressive rock, Psychedelic rock, Punk rock, Post-punk, New wave, Alternative rock, Indie rock, Grunge, Garage rock, Folk rock, Anatolian rock, Yugoslav rock
- **Metal**: Heavy metal, Thrash metal, Doom metal, Black metal, Folk metal, Power metal, Symphonic metal, Progressive metal
- **Pop**: Synth-pop, Dance-pop, Teen pop, Indie pop, Dream pop, Baroque pop, Chamber pop, City pop, J-pop, K-pop, C-pop, Mandopop, Cantopop, OPM, Europop, Italo pop
- **Soul**: Motown, Southern soul, Northern soul, Neo-soul
- **R&B**: Rhythm and blues (1940s–60s), Contemporary R&B
- **Funk**: P-funk, Brazilian funk (use **Funk carioca** as genre for Brazil)
- **Disco**: Italo disco, Hi-NRG
- **Hip-hop**: Boom bap, Trap, Conscious hip-hop, Drill, Grime (UK)
- **Electronic**: House, Techno, Trance, Drum and bass, Ambient, IDM, Electro, Synthwave, Dubstep, Amapiano (use Africa)

### Popular — Europe
- **Chanson**: Chanson française, Rive gauche
- **Variété française**
- **Schlager**: German Schlager, Volkstümlicher Schlager
- **Canzone napoletana**
- **Cantautori** (Italian singer-songwriter tradition)
- **Italo disco**
- **Fado**: Fado de Lisboa, Fado de Coimbra
- **Flamenco**: Bulerías, Soleá, Alegrías, Rumba flamenca, Nuevo flamenco
- **Copla**
- **Celtic**: Irish traditional, Scottish traditional, Breton, Galician, Celtic rock
- **Nordic folk**: Swedish polska, Norwegian hardingfele music, Finnish runo song, Joik (Sámi)
- **Polka**
- **Waltz**: Viennese waltz, Musette waltz
- **Klezmer**
- **Romance (Russian romans)**
- **Bard song** (avtorskaya pesnya)
- **Estrada** (Soviet and post-Soviet pop)
- **Eurovision pop** may be noted in `secondary_associations` only.

### Balkans and Southeast Europe
- **Sevdalinka**
- **Starogradska muzika** (old urban song)
- **Tamburica**
- **Izvorna muzika** (rural traditional)
- **Kolo** (dance melodies; also Oro, Horo, Hora as local names)
- **Balkan brass**: Serbian trumpet (Guča), Macedonian Romani brass
- **Narodna muzika** (newly composed folk music)
- **Turbo-folk**
- **Pop-folk** (Bulgarian chalga, Romanian manele: use the local name as subgenre)
- **Lăutărească**
- **Doina**
- **Laïko**, **Rebetiko**, **Entechno**, **Nisiotika**, **Dimotiko**
- **Yugoslav rock** and **Yugoslav new wave** go as subgenres under Rock; ex-Yu pop goes under **Pop**.
- **Klapa** (Dalmatian a cappella)
- **Ganga** and **Ojkanje** (traditional vocal forms)
- **Albanian iso-polyphony**
- **Bulgarian vocal polyphony**

### Latin America and the Caribbean
- **Mariachi**, **Ranchera**, **Norteño**, **Banda**, **Corrido**, **Son jarocho**, **Huapango**, **Bolero**, **Bolero ranchero**, **Cumbia** (subgenres: Colombian, Mexican, Peruvian chicha, Argentine villera)
- **Son cubano**, **Salsa**, **Mambo**, **Cha-cha-chá**, **Danzón**, **Rumba (Cuban)**, **Guaracha**, **Timba**, **Nueva trova**
- **Bachata**, **Merengue**, **Reggaeton**, **Plena**, **Bomba**
- **Mento**, **Ska**, **Rocksteady**, **Reggae**, **Dub**, **Dancehall**
- **Calypso**, **Soca**, **Steelpan music**, **Kompa**, **Zouk**, **Punta** (Garifuna)
- **Samba**, **Bossa nova**, **MPB**, **Choro**, **Forró**, **Baião**, **Frevo**, **Sertanejo**, **Axé**, **Funk carioca**, **Tropicália**
- **Tango**, **Milonga**, **Nuevo tango**, **Chacarera**, **Zamba (Argentine)**, **Candombe**, **Murga**
- **Vallenato**, **Joropo**, **Cueca**, **Huayno**, **Música criolla** (Peru), **Afro-Peruvian**, **Andean**, **Nueva canción**, **Rock en español**, **Latin pop**
- **Guarania**, **Polca paraguaya**, **Kaseko**, **Saya**, **Pasacalle**, **Danzante**, **Pasillo**, **Música llanera**, **Carnavalito**, **String band** (Guyana)

### Africa
- **Highlife** (subgenres: Palm-wine / guitar-band, Dance band, Burger), **Afrobeat** (Fela Kuti lineage), **Afrobeats** (21st-century pop), **Jùjú**, **Fuji**, **Apala**
- **Mbalax**, **Griot music** (subgenres: Mande kora, Wassoulou), **Desert blues**, **Mandingue**
- **Soukous**, **Congolese rumba**, **Ndombolo**, **Makossa**, **Bikutsi**, **Coupé-décalé**
- **Benga**, **Taarab**, **Bongo Flava**, **Kadongo kamu**
- **Ethio-jazz**, **Ethiopian popular music** (subgenres: tizita, ambassel modes)
- **Mbaqanga**, **Marabi**, **Kwela**, **Isicathamiya**, **South African jazz**, **Kwaito**, **Amapiano**, **Gqom**
- **Chimurenga**, **Sungura**, **Kalindula**, **Zamrock**
- **Semba**, **Kizomba**, **Kuduro**, **Marrabenta**, **Morna**, **Coladeira**
- **Raï**, **Gnawa**, **Chaabi**, **Andalusian classical (Maghreb)**, **Shaabi (Egypt)**, **Arabic classical**, **Salegy**, **Sega**

### Middle East, Turkey, Caucasus, Central Asia
- **Arabic pop**, **Arabic classical** (subgenres: Tarab, Muwashshah, Qasida), **Khaliji**, **Dabke**, **Mahraganat**
- **Persian classical** (subgenres: Radif, Dastgah), **Persian pop**
- **Turkish classical (makam)**, **Turkish folk (türkü)**, **Arabesk**, **Turkish pop**, **Anatolian rock**
- **Mizrahi**, **Israeli folk (Shirei Eretz Yisrael)**
- **Armenian folk**, **Georgian polyphony**, **Mugham**, **Ashik music**
- **Shashmaqam**, **Kazakh küy**, **Kyrgyz komuz music**, **Uzbek estrada**

### South Asia
- **Filmi** (subgenres: Bollywood, Tamil film music, Telugu film music, Lollywood)
- **Hindustani classical** (subgenres: Khayal, Dhrupad, Thumri), **Carnatic** (subgenres: Kriti, Varnam)
- **Ghazal**, **Qawwali**, **Bhajan**, **Kirtan**, **Sufi folk**
- **Bhangra**, **Indipop**, **Pakistani pop**, **Indian rock**, **Indie (India)**, **Coke Studio** recordings: note under `secondary_associations`
- **Rabindra Sangeet**, **Nazrul Geeti**, **Baul**, **Baila** (Sri Lanka), **Sinhala nurthi**, **Nepali folk (lok geet)**, **Nepali adhunik**

### East Asia
- **J-pop**, **J-rock**, **City pop**, **Enka**, **Kayōkyoku**, **Visual kei**, **Shibuya-kei**, **Vocaloid**
- **Japanese traditional** (subgenres: Min'yō, Gagaku, Shakuhachi honkyoku, Koto music, Nagauta)
- **K-pop**, **Korean ballad**, **Trot**, **K-indie**, **Korean traditional** (subgenres: Pansori, Minyo, Sanjo, Jeongak, Arirang variants)
- **Mandopop**, **Cantopop**, **C-pop**, **Chinese rock**, **Chinese traditional** (subgenres: Guqin, Erhu, Pipa, Jiangnan sizhu, Kunqu, Peking opera)
- **Mongolian traditional** (subgenres: Long song, Khöömii, Morin khuur), **Mongolian rock**

### Southeast Asia
- **Dangdut**, **Kroncong**, **Jaipongan**, **Pop Indonesia**, **Gamelan** (subgenres: Javanese, Balinese, Sundanese degung)
- **OPM**, **Kundiman**, **Pinoy rock**
- **Luk thung**, **Mor lam**, **T-pop**, **Thai classical (piphat)**
- **V-pop**, **Vietnamese traditional** (subgenres: Ca trù, Quan họ, Cải lương, Nhạc vàng, Nhạc trữ tình)
- **Cambodian rock** (1960s–70s), **Khmer traditional**
- **Malay pop**, **Ghazal (Malay)**, **Joget**, **Xinyao** (Singapore)
- **Shan popular song** (Myanmar)

### Oceania
- **Australian rock**, **Pub rock**, **Indigenous Australian** (subgenres: Songlines, Yolŋu contemporary, Didgeridoo)
- **Māori** (subgenres: Waiata, Haka, Contemporary Māori)
- **Pacific reggae**, **Polynesian traditional**, **String band (Pacific)**, **Hawaiian music** (if included, `country = United States`, region Oceania noted)

### Jazz
- **Jazz** with subgenres: Dixieland, Swing, Bebop, Cool jazz, Hard bop, Modal jazz, Free jazz, Jazz fusion, Latin jazz, Bossa jazz, Gypsy jazz (Manouche), Nordic jazz, Ethio-jazz, Cape jazz, Jazz standard, Great American Songbook

### Western art music (`classical_historical.csv`)
- **Baroque**, **Classical period**, **Romantic**, **Impressionism**, **Nationalism (music)**, **Modernism**, **Minimalism**, **Neoclassical (contemporary)**, **Contemporary classical**
- **Opera** (subgenres: Opera seria, Opera buffa, Bel canto, Verismo), **Operetta**, **Ballet**, **Art song (Lied, Mélodie)**, **Zarzuela** (or Musical theatre/Stage)
- **Historical popular melody** (parlour song, broadside ballad, early dance tunes)

### Soundtrack and game music
- **Film score** (subgenres: Orchestral, Electronic, Minimalist, Spaghetti western, Bollywood background score)
- **Film song**, **TV theme**, **Anime theme** (subgenres: Opening, Ending, Insert song), **Animation song** (Disney, Soviet animation…)
- **Musical theatre** (subgenres: Broadway, West End, Rock musical, Sung-through)
- **Video game music** (subgenres: Chiptune, Orchestral, JRPG, Platformer, Indie game, Rhythm game)

---

## 5. Region labels used in `region`

Use these where they fit; finer labels are welcome in `subgenre` or the notes.

North America · Mexico · Central America · Caribbean · Andes · Southern Cone · Amazon · Brazil · Western Europe · Southern Europe · Northern Europe · Central Europe · Eastern Europe · Balkans / Southeast Europe · North Africa · West Africa · Central Africa · East Africa · Horn of Africa · Southern Africa · Indian Ocean · Levant · Arabian Peninsula · Mesopotamia · Iran · Anatolia · Caucasus · Central Asia · South Asia · East Asia · Southeast Asia (Mainland) · Southeast Asia (Maritime) · Australia · New Zealand · Melanesia · Polynesia · Micronesia · International (for global productions such as Hollywood films).
