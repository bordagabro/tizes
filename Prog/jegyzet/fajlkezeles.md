# Fájlkezelés

*Fájl megnyitása*
    open("fájlnév", "mód")

*4 féle mód van:*
    - **r** - read, megnyitás olvasásra (alapértelmezett), ha nincs fájl -> hiba
    - **a** - append, megnyitás hozzáfűzésre, ha nincs fájl létrehozza
    - **w** - write, megnyitás írásra, ha nincs fájl létrehozza
    - **x** - létrehozza a fájlt, ha lézetik -> hiba

*Ezen felül megadhatjuk, hogy bináris vagy szöveges fájl
    - **t** - text mode (alapértelmezett)
    - **b** - binary mode

## Fájl megnyitása:
    open("demofile.txt")
    open("demofile.txt", "rt")