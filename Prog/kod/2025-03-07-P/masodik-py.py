fajl = open("/home/borda/oskola/tizes/Prog/kod/2025-03-07-P/szamok.txt", "r", encoding="utf-8")
fajl2 = open("/home/borda/oskola/tizes/Prog/kod/2025-03-07-P/szamok-out.txt", "w", encoding="utf-8")

szamok = fajl.readlines()

i = 0
while(i < len(szamok)):
    fajl2.write(f"{szamok[i].strip()} {szamok[i+1].strip()} {szamok[i+2].strip()}\n")
    i += 3

fajl.close()
fajl2.close()









