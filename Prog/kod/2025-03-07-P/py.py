fajl = open("/home/borda/oskola/tizes/Prog/kod/2025-03-07-P/vers.txt", "r", encoding="utf-8")
sorok = fajl.readlines()
sorokSzama = len(sorok)

with open("szoftverfejleszto.txt", "w") as szvfejl:
    for sor in sorok:
        szavak = sor.split(" ")
        for szo in szavak:
            if("szoftverfejlesztő" in szo):
                szvfejl.write(sor)

def leghosszabb_sor():
    rtr = 0
    rtrLen = 0
    for i in range(sorokSzama):
        sor = sorok[i]
        if(len(sor) > rtrLen):
            rtrLen = len(sor)
            rtr = i + 1
    return rtr

def megszamlal():
    rtr = 0
    for i in range(sorokSzama):
        sor = sorok[i]
        szavak = sor.split(" ")
        for szo in szavak:
            if("szoftver" in szo):
                rtr += 1

    return rtr

def eldontes():
    talalt = False
    for i in range(sorokSzama):
        sor = sorok[i]
        if(len(sor) == 25):
            talalt = True
    return talalt

print("Leghosszabb szó:", leghosszabb_sor())
print("Szoftver szó előfordulása (db):", megszamlal())
print("Van -e olyan sor ami 25 karaktert tartalmaz (True/False):", eldontes())

fajl.close()






