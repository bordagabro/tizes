tablazat = open("/home/borda/oskola/tizes/Prog/kod/2025-03-07-P/harmadik-feladat-szamok.txt", "r", encoding="utf-8")
sorok = tablazat.readlines()
matrix = []

for sor in sorok:
    oszlopok = sor.split(" ")
    matrix.append(oszlopok)


def lekeres(sor, oszlop):
    return(matrix[sor][oszlop].strip())


print(lekeres(int(input("Sor: >> "))-1, int(input("Oszlop: >> "))-1))

tablazat.close()






# FÉLREÉRTETTEM A FELADATOT NE MÁSOLD








