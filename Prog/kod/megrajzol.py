def megrajzol(x, y):
	for i in range(1, 4):
		for j in range(1, 7):
			if x == i and y == j:
				print("+", end=" ")
			else:
				print("0", end=" ")
		print()

x = int(input("Hányadik sorba (1-3) tegyük a +-t?"))
y = int(input("Hányadik oszlopba (1-6) tegyük a +-t?"))

megrajzol(x, y)

