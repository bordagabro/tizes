# Szótár

- szöveges vagy szám tipúsúak
- Minden kulcs egyedi kell legyen
- A kulcs lehet *int* vagy *string*
- A pároknak nincs sorszámunk, nem index, hanem **kulcs** alapján kell menni.

*dictionary = {"cat": "macska", "dog": "kutya", "horse": "ló"}*
*tel_szamok = {"anya": "06/30-123-4567", "miki": "06/20 BUZ-I420"}*
*ures = {}*

- Használhatjuk a **len()** függvényt a párok számát adja meg
- Használjhatjuk a **print()** függvényt, ami egy az egyben kipakolja nekünk az értékpárokat.
	- *print(dictionary)*
	- *print(dictionary["cat"])*
	

- For ciklussal bejárható:
	*
	for key in dictionary.keys():
		print(key, "->", dictionary[key]
	*
- Ha rendezve akarjuk látni:
	*
	for key in sorted(dictionary.keys()):
		print(key, "->", dictionary[key]
	*
- A párokat így is kiirhatjuk:
	*
	for angolul, magyarul in dictionary.items():
		print(angolul, "->", magyarul)	
	*
- Ha csak az értékeket írjuk ki:
	*
	for magyarul in dictionary.values():
		print(magyarul)


	\>>> cat -> macska
	\>>> dog -> kutya
	\>>> horse -> ló
	*
- Érték megváltoztatása:
	*
	dictionary["cat"] = "cica"
	*
- Új pár hozzáadása:
	*
	dictionary["lion"] = "oroszlán"
	*vagy*
	dictionary.update()
	*
- Adott pár törlése:
	*
	del dictionary["dog"]
	*
- Rendezés értékek alapjan
	*
	szotar = {"a": 2, "b": 1, "c": 3}	
	for w in sorted(szotar, key=szotar.get, reverse = True)
	*
## Gyakoriság figyelése
	*
	nevek = ["Piri", "Peti", "Pali", "Piri", "Piri", "Pali"]
	szotar = {}
	for elem in nevek
		if elem in szotar:
			szotar[elem] + 1
		else:
			szotar[elem] = 1

	*
