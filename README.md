# funfair

This is a game that happens in a small town where funfair arrives.

Written in Python. Uses SQL database.

## Pelin rakenteen suunnittelua

Muutama sananen rakenteesta...

## TODO

* ~~DB: Items -> Item types (Dmitri)~~ **Done**
* ~~utils.print_text() syö välilyöntejä, fix (Dmitri)~~ **Done**
* ~~utils.print_text() str.center(150) (Dmitri)~~ **Done**
* ~~pelajan nimen syöttö tietokantaan (Dmitri)~~ **Done**
* ~~tips: eka tip tulee heti. (give_tip() tarkistaa, onko first_tip TRUE) (Heikki)~~ **Done**
* tips: päivät vaikuttavat todennäköisyyteen **(Heikki)**
* ~~tips: arvotaanko vihjeitä myös hahmoille, joiden kanssa ei voi jutella? (Director) (Heikki)~~ **Done**
* Games: pelien siirto tietokantaan tai omat aliohjelmat? **(Heikki, Suvi)**
* ~~EAT (Suvi~~ **(Done)**
* ~~BUY (Suvi)~~ **(Done)**
* ~~DRINK (Suvi)~~ **(Done)**
* Campfire: interaktiivinen? **(Heikki)**
* Epilogi campfiren jälkeen **(Heikki)**
* Passages: locked=true **(Heikki)**
* ~~HELP (Suvi)~~ **(Done)**
* ~~HELP [command] (Dmitri)~~ **Done**
* Inventory **(Dmitri)**
* Inventory listaa vihjeet **(Heikki)**
* ~~GO, WALK, pitkät versiot ilmansuunnista (Heikki)~~ **Done**
* ~~Directions kertomaan, mihin ilmansuunnat vievät (Dmitri)~~ **Done**
* ~~RIDE tarkistettava, funktion on tarkistettava onko lippu. (Suvi)~~**(Done)**
* ~~Sanomalehden tekstit tietokannasta (Dmitri)~~ **(Done)**

* Lisää tavaraa tietokantaan **(Dmitri, Heikki, Suvi)**


###Parser

**Parser** palauttaa sanakirjan: {'indirect_place_id': 6, 'verb': 'ask', 'object': 'elna', 'direct_person_id': 1, 'indirect': 'carousel'} missä *verb* on verbi, *object* on objekti ja *indirect* on epäsuora objekti. 
*direct_person_id* on suoran henkilön id tietokannassa aliaksella haettu ja *indirect_place_id* on epäsuoran paikan id tietokannasta aliaksella haettu.

Suoria voivat olla:

*direct_person_id* - henkilön id aliaksella haettu

*direct_item_id* - esinen id aliaksella haettu, voi olla useita

*direct_place_id* - paikan id aliaksella haettu

Epäsuoria voivat olla:

*indirect_person_id* - henkilön id aliaksella haettu

*indirect_item_id* - esinen id aliaksella haettu, voi olla useita

*indirect_place_id* - paikan id aliaksella haettu

Jokainen verbi on oma aliohjelmansa. talk(), ask() jne

Parserin palauttama sanakirja prosessoidaan ja tehdään valinta, mitä aliohjelmaa kutsutaan. Aliohjelmalle annetaan *object* ja *indirect_object*

### Vihjeet
Tehdään **vihjemoduuli**, joka pitää kirjaa vihjeistä
Pelin alussa kutsutaan arpominen: *tips.create_connections()*. Tämä aliohjelma arpoo, ketkä henkilöt pitävät toisistaan.
Pelin tai päivän alussa kutsutaan *tips.generate_tips*

Talk-phasessa kutsutaan tips-moduulia esim näin: *tips.give_tip()*
give_tip -aliohjelma sitten ratkaisee, antaako se tässä keskustelussa vihjeen vai ei. Se myös päättää, antaako tosi vihjeen vai paikkansapitämättömän vihjeen.
Aliohjelma palauttaa valmiiksi muotoillun vihjeen, jos vihjeitä on jäljellä. Vaihtoehtoisesti ei mitään.

### Päivät ja kyselyt
Tehdään *days*-muuttuja, joka laskee päivien määrää.

Tehdään *asks*-muuttuja, joka laskee, montako kertaa on kysytty

Kun pelaaja yrittää tehdä connectionin sanomalla
<pre>ASK Elna to Carousel</pre>
*asks*-muuttujan arvoa kasvatetaan yhdellä.

Jos *asks* >= 2, ajetaan
*nighttime()*-aliohjelma, joka tulostaa tietoa yöstä, ja tekee muuttujia:
*asks* nollataan, *days* kasvaa yhdellä.

Jos *days* > 3, mennään loppuvaiheeseen, joka on oma aliohjelmansa
final()

### Campfire
Campfire on oma erillinen looppinsa. Siellä voi puhua kaikille eri henkilöille.
Jos campfirellä puhuu Ferris Wheel -operatorille, pääsee maailmanpyörään.

## Moduulit
* **lib/database.py** - tietokannan yhteys, kytketään käskyllä 
<pre>from lib.database import FunDb
connect=FunDb.connect()</pre>
jonka jälkeen tietokantaan otettaan yhteyttä "connect"-muuttujan kautta, esim "cur=connect.cursor()"
* **globals.py** - tallettaa globaalit muuttujat, joita kutsutaan kaikista moduuleista

    *Muista aina moduulin alkuun:*
    <pre>import globals</pre>
    *Ja muuttujia kutsutaan:*
    <pre>globals.verbs</pre>
* **parser.py** - Sisältää parserin
* **tips.py** - Vihjemekaniikka
* **main.py** Pelin päämoduuli, joka kutsuu kaikkia muita
