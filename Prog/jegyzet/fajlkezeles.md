# Fájlkezelés

*Fájl megnyitása:*
	open("fájlnév", "mód")

*4 féle mód van:*
- **r** - read, megnyitás olvasásra (alapértelmezett), ha nincs fájl -> hiba
- **a** - append, megnyitás hozzáfűzésre, ha nincs fájl létrehozza
- **w** - write, megnyitás írásra, ha nincs fájl létrehozza
- **x** - létrehozza a fájlt, ha lézetik -> hiba

Ezen felül megadhatjuk, hogy bináris vagy szöveges fájl
- **t** - text mode (alapértelmezett)
- **b** - binary mode

## Fájl megnyitása:
    open("demofile.txt")
    open("demofile.txt", "rt")


## Olvasás:
    f = open("demofile.txt", "r")
    print(f.read())

    f.readlines() -> a teljes fájlt olvassa be, a sorokat listába rendezi E8FF-C9F7

Ha nem akarjuk a teljes fájlt beolvasni:

    print(f.read(5))

    print(f.readline())

    for sor in f:
        print(sor)

## Fájl bezárása:
    f.close() -> A VÁLTOZTATÁSOK CSAK EKKOR MENTŐDNEk

## Fájlba írás:
- "a"  - A fájl véghéhez hozzáfűz
- "w"  - Felülírja a fájl tartalmait

    f = open("demofile.txt", "a")
    f.write("Így adhatok hozzá a fájlhoz")
    g = open("demofile2.txt", "w")
    g.write("Így írom felül az eddigi tartalmakat")


Írás után mindenkép használjuk: close()

    with open("file", "mode") as var:
        blokk, melyben a fájllal dolgozok (behúzás mint ciklusnál)
    print("Itt már be van zárva")
