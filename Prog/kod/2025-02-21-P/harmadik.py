with open("adatok.txt", "r") as regi:
    with open("legujabbadatok.txt", "w") as uj:
        for i in regi:
            if "info" in i:
                uj.write(i)

print(":D")