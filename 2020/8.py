import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)

j = 0
i = 0
reg = 0
part1 = False
visited = []
lenght = len(lines)
lines_copy = list(lines)

while 1:
	if i >= lenght:
		print(reg)
		break
	if i in visited:
		if not part1:
			print(reg)
			part1 = True
		i = 0
		reg = 0
		visited = []
		lines = list(lines_copy)
		while 1:
			words = lines[j].split()
			if words[0] == 'nop':
				lines[j] = 'jmp ' + words[1]
				break
			elif words[0] == 'jmp':
				lines[j] = 'nop ' + words[1]
				break
			else:
				j += 1
		j += 1
		continue
	visited.append(i)
	words = lines[i].split()
	if words[0] == 'jmp':
		i += int(words[1]) 
	else:
		if words[0] == 'acc':
			reg += int(words[1])
		i += 1
