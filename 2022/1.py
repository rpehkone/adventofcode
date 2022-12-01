import sys

f = open(sys.argv[1], 'r', encoding = "utf-16")
file = f.read().splitlines()

this = 0
elfs = []
for line in file:
	line = line.strip()
	if not line:
		elfs.append(this)
		this = 0
	else:
		this = this + int(line)
elfs.sort()
print("part1: " + str(elfs[-1]))
print("part2: " + str(sum(elfs[-3:])))
