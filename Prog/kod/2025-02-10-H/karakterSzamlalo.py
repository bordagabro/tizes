# Olvassunk be egy szöveget. Számoljuk meg,  hogy melyik karakter hányszor fordul elő.

szoveg = input("Kérem a szöveget! >> ")			# Szöveg bekérése, tárolása a szöveg változóban
szamlalo = {}						# Üres szótár létrehozása

for i in szoveg:					# Vég(h)ig megyünk a szöveg betűin
	if i in szamlalo:				# Ha a betű már szerepel a szótárban
		szamlalo[i] = szamlalo[i] + 1;		# Hozzáadunk egyet a hozzá rendelt értékhez
	else:						# Ha nem szerepel
		szamlalo[i] = 1;			# Létrehozzuk és az 1 értéket rendeljük hozzá.


for i in szamlalo.keys():				# Vég(h)ig megyünk a szótár kulcsain (jelenleg betűk)
	print(i, "->", szamlalo[i])			# És kiírjuk a betűket és a hozzá tartózó értéket
