# Megszámoljuk, hogy hány név hányszor szerepel

nevek = ["Karcsi", "Elemér", "Kiss Miklós", "János", "Kiss Miklós", "Karcsi", "Karcsi"]
szamlalo = {};

for i in nevek:						# Vég(h)ig megyünk a 'nevek' listán
	if i in szamlalo:				# Ha a most vizsgált név már benne van a 'szamlalo' szótárban
		szamlalo[i] = szamlalo[i] + 1; 		# Hozzáadunk a névhez rendelt értékhez egyet
	else:						# De ha nincs
		szamlalo[i] = 1;			# Hozzáadjuk a nevet a szótárhoz 1 értékkel (ez az első)

print(nevek)
print(szamlalo)
