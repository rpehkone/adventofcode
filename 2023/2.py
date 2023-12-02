import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()

part1 = 0
part2 = 0
for line in lines:
	game_id = int(line.split(":")[0].split(" ")[1])
	game = line.split(":")[1][:-1].replace(";", ",").split(",")

	r = 0
	g = 0
	b = 0
	possible = True
	for set in game:
		n = int(set.strip().split(" ")[0])
		if "red" in set:
			if n > 12:
				possible = False
			r = max(r, n)
		elif "green" in set:
			if n > 13:
				possible = False
			g = max(g, n)
		elif "blue" in set:
			if n > 14:
				possible = False
			b = max(b, n)
	if possible:
		part1 += game_id
	part2 += r * g * b

print("part1:", part1)
print("part2:", part2)
