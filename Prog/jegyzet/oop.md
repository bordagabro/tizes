# OOP - Objektum Orientált Programozás

**Objektumorientált programozaás**
Szoftverfejlesztési módszer, melyben a problémát (rendszert) a való világ tárgyaihoz (objektumaihoz) hasonlatosan önálló, önmagukban zárt, de egymással interakcióra képes elemekre bontva oldjuk meg. 

**Előnyök**
- kód átláthatósága, újrahasznosíthatósága
- program rugalmasabb, biztonságos alakítása a későbbi igények esetén
- ha tövv programozó dolgozik egy programon kevesebb 'veszélyt' jelent

**Osztály:** azonos tulajdonságokkal (jellenzőkkel) és viselkedéssel rendelkező egyedeket zárja be egy egységbe.
- A tulajdonságok értékét adatok (attribútomok) tárolják.
- A viselkedéseket pedig a metódusok írják le.

**Objeltum**: az osztály egy példánya, egyede (osztály tipusú változó)

**ADATOK + METÓDUSOK = OSZTÁLY**

Az osztály adattípus, amely egy adott jellegű objektum ,,sablondefiníciójaként" szolgál.
pl.:
**Osztály:**
Parkolóban sok künönbözőp autó, mindnek van típusa, gyártója, színe, évjárata, mind tud indulni, megállni, lehet tankolni stbv.

**Objektum:**
A fenti tulajdonságokhoz értéket rendelünk, egy konkrét autót adunk meg.
Az objektum egy osztály típusú változó.

## Osztály létrehozása

    class név:
        //nem maradhat üresen, pass, vagy 1 sornyi osztályt leíró karakterlánc lerül, ezt megjegyzésnek tekinti

    // pl.:
    class Ember:
        "egy ember definíciója"

**Ezt konstruktor követi**

    class Ember:
        def __init__(self, nev):        // KONSTRUKTOR
            self.neve = nev             // KONSTRUKTOR   
            self.xpoz = 0               // KONSTRUKTOR
            self.ypoz = 0               // KONSTRUKTOR

    ember = Ember("Pista")
    print(ember.neve)
    print(ember.xpoz)