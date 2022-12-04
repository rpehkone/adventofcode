import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)

part1 = 0
part2 = 0
for line in lines:
	line = line.strip()
	words = line.split(',')
	l = words[0].split('-')
	r = words[1].split('-')
	ls = int(l[0])
	le = int(l[1])
	rs = int(r[0])
	re = int(r[1])
	if ls >= rs and le <= re:
		part1 = part1 + 1
	elif ls <= rs and le >= re:
		part1 = part1 + 1
	if ls >= rs and ls <= re:
		part2 = part2 + 1
	elif le >= rs and le <= re:
		part2 = part2 + 1
	elif rs >= ls and rs <= le:
		part2 = part2 + 1
	elif re >= ls and re <= le:
		part2 = part2 + 1
print("part1: " + str(part1))
print("part2: " + str(part2))
