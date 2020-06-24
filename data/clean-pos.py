strings = ("???", "***", "ERROR", "err", "PRONÃ§", "E3S?PERS", "B'IK", " ,", ", ", ",\n", "*", "(", "[", "/")

infile = "pos_dict.csv"

outfile = "pos_dict-cleaned.csv"

cleaned = []
with open(infile, "r") as file:
	for line in file:
		if any(s in line for s in strings):
			pass
		elif line[0] == ',':
			pass
		else:
			cleaned.append(line)

with open(outfile, "w") as file:
	for line in cleaned:
		file.write(line)
