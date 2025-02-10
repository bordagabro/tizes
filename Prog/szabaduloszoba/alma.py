def szavak_szama(mondat):
	szavakSzama = 1;
	for ly in mondat:
		if ly == " ":
			szavakSzama += 1;
	return szavakSzama;

def leghosszab_szo_hossza(mondat):
	szavakHossza = [];
	hosszSzamlalo = 0;
	for ly in mondat:
		if ly == " ":
			szavakHossza.append(hosszSzamlalo)
			hosszSzamlalo = 0;
		else:
			hosszSzamlalo += 1;

	szavakHossza.append(hosszSzamlalo);
	leghosszabb = 0;
	for dzs in szavakHossza:
		if dzs > leghosszabb:
			leghosszabb = dzs;

	return leghosszabb;

def osszeg(arr):
	osszeg = 0;
	for k in arr:
		osszeg += k

	return osszeg;

def nyolcal_oszthato(arr):
	szamlalo = 0;
	for k in arr:
		if k % 8 == 0:
			szamlalo += 1;
	return szamlalo;

def harommal_oszthato(arr):
	szamlalo = 0;
	for k in arr:
		if k % 3 == 0:
			szamlalo += 1;
	return szamlalo;

lista = [];
szoveg = "Ez a relytélyes szöveg segít a titkos kód megtalálásában";

for cs in range(szavak_szama(szoveg)):
	if(cs == 0):
		lista.append(leghosszab_szo_hossza(szoveg));
	else:
		lista.append(lista[cs-1] * 2)


if(osszeg(lista) > 30000):
	print(nyolcal_oszthato(lista));
else:
	print(harommal_oszthato(lista));
