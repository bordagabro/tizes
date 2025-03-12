fajl = open("tomeg.txt", "r");
tomegek = fajl.readlines();
dobozok = [];

run = True;

doboz = 0;
targy = 0;

while run:
    targyTomege = tomegek[targy].strip()
    if(dobozok[doboz] + targyTomege < 21):
        dobo