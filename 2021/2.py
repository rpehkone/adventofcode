import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)

x = 0
y1 = 0
y2 = 0
for line in lines:
	words = line.split()
	n = int(words[1])
	if words[0] == "forward":
		x += n
		y2 += y1 * n
	elif words[0] == "up":
		y1 -= n
	elif words[0] == "down":
		y1 += n

print(x * y1)
print(x * y2)
