fajl = open("tomeg.txt", "r")
targyak = fajl.readlines()

doboz = [0]
futoDoboz = 0

osszSuly = 0
for targy in targyak:
    targy = int(targy.strip())
    osszSuly += targy

for targy in targyak:
    targy = int(targy.strip())
    if(doboz[futoDoboz] + targy < 21):
        # print(f"Doboz: {futoDoboz} Doboz tömege: {doboz[futoDoboz]} Tárgy tömege: {targy} BELEFÉR")
        doboz[futoDoboz] += targy
    else:
        # print(f"Doboz: {futoDoboz} Doboz tömege: {doboz[futoDoboz]} Tárgy tömege: {targy} NEM FÉL BERE")
        futoDoboz += 1
        doboz.append(targy)

        
print("2. feladat:")
print("Tárgyak tömegének összege:", osszSuly)
print("3. feladat:")
print("Dobozok tartalmának tömege: (kg): ", end="")
dobozokDarab = 0
for i in doboz:
    dobozokDarab += 1
    print(i, end=" ")
print("\nSzűkséges dobozok száma:", dobozokDarab)
