with open("adatok.txt", "w") as f:
    for i in range(5):
        f.write(f"{i}. sor\n")

with open("adatok.txt", "a", encoding="utf-8") as g:
    g.write("Ez utólag került bele :3 \n")