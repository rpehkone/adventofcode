import fileinput

lines = []
for line in fileinput.input():
	lines.append(line.strip())

gamma = ""
epsilon = ""
for i in range(len(lines[0])):
	c = 0
	for line in lines:
		if line[i] == '0':
			c += 1
	if c > (len(lines)) / 2:
		epsilon += '1'
		gamma += '0'
	else:
		epsilon += '0'
		gamma += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print("e * g = " + str(epsilon * gamma))

def find_rating(p2oxy, invert):
	for i in range(len(lines[0])):
		c = 0
		for line in p2oxy:
			if line[i] == '0':
				c += 1
		type = '0'
		if invert:
			type = '1' if c > (len(p2oxy)) / 2 else '0'
		else:
			type = '1' if c <= (len(p2oxy)) / 2 else '0'

		if len(p2oxy) == 1:
			break
		drop = 1
		while drop:
			drop = 0
			for x, word in enumerate(p2oxy):
				if word[i] != type:
					del p2oxy[x]
					drop = 1
					break
	return int(p2oxy[0], 2)

oxygen = find_rating(lines.copy(), False)
co2 = find_rating(lines.copy(), True)
print("rating = " + str(oxygen * co2))
