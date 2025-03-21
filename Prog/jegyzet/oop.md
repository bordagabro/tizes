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

    ember = Ember("Pista")              // OBJEKTUM LÉTREHOZÁSA
    print(ember.neve)                   // >> Pista
    print(ember.xpoz)                   // >> 0

**Konstruktor:**
Speciális függvény, amely csak az objektum első létrehozásakor van meghívva. A konstruktor neve: __init__.
Első (vagy egyetken) paraméterként a self kulcsszót kell átadni a konstruktornakm ez arra szolgál, hogy azonosítsa az objektumok, amelyben meghívásra került, hogy hozzáférjen az objektum tulajdonságaihoz, metódusatihoz.
Nem ad vissza értéket, és nem lehet bármikor meghívni

**Osztály metódusai**

    Class Ember:
        def __init__(self, nev):
            self.neve = nev
            self.xpoz = 0
            self.ypoz = 0

        def mozog(self, x, y):
            self.xpoz += x
            self.ypoz += y

    ember = Ember("Béla")       // Ember osztály létrehozása ember változóban

    print(ember.xpoz)           // >> 0
    print(ember.ypoz)           // >> 0

    ember.mozog(1,4)            // Ember osztály mozog függvényének meghívása 1,4 értékkel

    print(ember.xpoz)           // >> 1
    print(ember.ypoz)           // >> 4

