class Dacia:
    def __init__(self, tipus, szin, tulaj, ajtok, kmOra):
        self.markaja = "Dacia"
        self.tipusa = tipus
        self.szine = szin
        self.tulaja = tulaj
        self.ajtok = ajtok
        self.allapota = "gurul"
        self.az_a_hely_ahova_beteszed = 0
        self.km = kmOra

    def tankol(self, uzemanyag_mennyiseg):
        self.az_a_hely_ahova_beteszed += uzemanyag_mennyiseg

    def megy(self, mennyit_megy):
        self.km += mennyit_megy


kivaloAuto = Dacia("Logan 2002", "Rozsda", "Tóth Feribácsi", 9, 20000)
print(kivaloAuto.az_a_hely_ahova_beteszed, "liter (használt) étolaj van a tankban.")

kivaloAuto.tankol(20)
print(kivaloAuto.az_a_hely_ahova_beteszed, "liter (használt) étolaj van a tankban. (töltés után)")

kivaloAuto.megy(120)
print(kivaloAuto.km, "métert gurult motor nélkül")
