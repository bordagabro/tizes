class Allat:
    def __init__(self, fajta, nev, suly):
        self.fajtája = fajta
        self.neve = nev
        self.sulya = suly
    
    def eszik(self, mennyisegg):
        self.sulya += mennyisegg

rufusz = Allat("Gugya", "Rufuszocska", 8.5)
geza = Allat("Ceca", "Gézuska", 3.2)

rufusz.eszik(3.2)
geza.eszik(0.3)

print(rufusz.neve,rufusz.sulya, "tonnás")
print(geza.neve,geza.sulya, "tonnás")