"""Készíts egy programot, amelyben van egy Negyzet nevű osztály. Adata lengyen az oldal hossza.
   Rendelkezzen továbbá a kerület és terület számítására os egy-egy metódussal!"""

class Negyzet:
    def __init__(self, oldal):
        self.a = oldal

    def kerulet(self):
        return self.a*4

    def terulet(self):
        return self.a**2


inp = int(input("Adja meg a négyzet oldalhosszát! >> "))

oldalak = []
keruletek = []
teruletek = []

while inp != 0:
    II_days_kocka = Negyzet(inp)
    print("Négyzet kerülete:", II_days_kocka.kerulet())
    print("Négyzet területe:", II_days_kocka.terulet())

    oldalak.append(inp)
    keruletek.append(II_days_kocka.kerulet())
    teruletek.append(II_days_kocka.terulet())

    inp = int(input("Adja meg a négyzet oldalhosszát! >> "))

    with open("Négyzetfájl.txt", "w") as IVzet_fajl:
        for i in range(len(oldalak)):
            IVzet_fajl.write(f"{str(oldalak[i])} oldalhosszú négyzet kerülete: {str(keruletek[i])}, területe: {str(teruletek[i])}\n")