szotar = {"kutya": 4, "tyúk": 2, "hal": 0, "százlábú": 100}

for kulcs, ertek in szotar.items():
	print(kulcs, "->", ertek)

for kulcs in sorted(szotar.keys()):
	print(">", kulcs)
