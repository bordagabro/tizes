dzs = open("adatok.txt", "r")
sorok = dzs.readlines()

masodik = open("adatokkk.txt", "w")

for i in range(len(sorok)):
    i2 = (len(sorok) - i) - 1
    masodik.write(sorok[i2])

dzs.close()
masodik.close()
