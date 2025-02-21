with open("adatok.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        f.write(f"{i+1}. sor\n")

with open("adatok.txt", "a", encoding="utf-8") as g:
    g.write("Ez utólag került bele :3 \n")

with open("adatok.txt", "r", encoding="utf-8") as h:
    print(h.readlines())

h = open("adatok.txt", "r")

for sor in h:
    print(">", sor)