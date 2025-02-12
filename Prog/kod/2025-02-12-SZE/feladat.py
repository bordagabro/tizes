# Jelöltek: max10
# Szavazásra jogosultak: max20

def getKey(val):
	for i in szavazatok.keys():
		if(szavazatok[i] == val and i not in getKeyTemp):
			getKeyTemp.append(i);
			return i;
getKeyTemp = []
jeloltek = int(input("Jelöltek száma (max.10): "));
szavJog = int(input("Szavazásra jogosultak száma (max.20): "));
nemJo = 0;
szavazatok = {}


if(jeloltek < 1 or jeloltek > 10):
	print("Érvénytelen a jelöltek száma :c");

elif(szavJog < 1 or szavJog > 20):
	print("Érvénytelen a szavazásra jog. száma :c");
else:
	lSzaml = 0;
	run = True;
	while (lSzaml < szavJog and run):
		tSzav = int(input(f"Adja meg az {lSzaml + 1}. szavazatot! "));
		if(tSzav > jeloltek):
			print("ÉRVÉNYTELEN SZAVAZAT!!!");
			nemJo += 1;
		elif(tSzav < 1):
			run = False;
			print("BEKÉRÉS LEÁLLÍTVA!")
		else:
			if(tSzav not in szavazatok):
				szavazatok[tSzav] = 1;
			else:
				szavazatok[tSzav] = szavazatok[tSzav] + 1;
		lSzaml += 1;

print("------------------------");
print("       EREDMÉNYEK       ");
print("------------------------");

print("Szavazatra jogosultak száma:", szavJog);
print("Összes leadott szavazat száma:", lSzaml - 2);
print("Érvényes szavazatok száma:", lSzaml - nemJo - 1);
print("Érvénytelen szavazatok száma:", nemJo - 1);

ervenyesPrc = ((lSzaml - nemJo) * 100) / szavJog;

if(ervenyesPrc > 0):
	print(f"Érvényes szavazatok százaléka: {ervenyesPrc}%, a szavazás érvényes");
else:
	print(f"Érvényes szavazatok százaléka: {ervenyesPrc}%, a szavazás érvénytelen");

print("Jelöltek eredményei:")
print("Helyezés		Jelölt sorszáma		Szavazatszám 		Szavazat arány")

hely = 0;
for i in sorted(szavazatok.values(), reverse = True):
	hely += 1;
	print(f"{hely}			{getKey(i)}			{i}			{(i * 100) / lSzaml - lSzaml - 2}%")
