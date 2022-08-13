import fileinput

lines = []
for line in fileinput.input():
	lines.append(line.strip().split('-'))

caves = {}
seen = []

def caveadd(name):
	if name in seen or name == 'end':
		return
	seen.append(name)
	tmp = []
	for line in lines:
		if line[0] == name and line[1] != 'start':
			tmp.append(line[1])
		if line[1] == name and line[0] != 'start':
			tmp.append(line[0])
	caves[name] = tmp

for line in lines:
	caveadd(line[0])
	caveadd(line[1])

part1 = []
path = []

def caverun1(name):
	for c in caves[name]:
		if c.isupper() or c not in path:
			path.append(c)
			if c == 'end':
				part1.append(path[:])
			else:
				caverun1(c)
			path.pop()

twiceactive = ""
part2 = []

def caverun2(name):
	global twiceactive

	for c in caves[name]:
		canadd = False
		if c.isupper():
			canadd = True
		else:
			num = path.count(c)
			if num == 0:
				canadd = True
			elif num == 1:
				if twiceactive == "":
					twiceactive = c
					canadd = True
		if canadd:
			path.append(c)
			if c == 'end':
				part2.append(path[:])
			else:
				caverun2(c)
			num = path.count(c)
			if num == 2 and path[-1] == twiceactive:
				twiceactive = ""
			path.pop()

caverun1('start')
print(len(part1))
path = []
caverun2('start')
print(len(part2))
