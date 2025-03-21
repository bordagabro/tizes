import random

class Gugya:
    def __init__(self, nev):
        self.nev = nev
        if(random.randint(0,1)):
            self.nem = "hím"
        else:
            self.nem = "nőstény"
        self.kor = random.randint(0,16)

    def prNem(self):
        return self.nem
    
    def prNev(self):
        return self.nev

    def prKor(self):
        return self.kor

kiskutyákok = []

run = True
while(run):
    neve = input("Adja meg a kutya nevét! (az utolsó kutya után küldj ;-t) >> ")
    if(";" in neve):
        run = False
    else:
        blöki = Gugya(neve)
        kiskutyákok.append(blöki)

with open("kizsgugyákok.txt", "w") as fajl:
    for i in kiskutyákok:
        fajl.write(f"Név: {i.prNev()}, Kor: {i.prKor()}, Nem: {i.prNem()}\n")    