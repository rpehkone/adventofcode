from copy import deepcopy
import fileinput

inputfile = []
for line in fileinput.input():
	new = []
	[new.append(c) for c in line]
	inputfile.append(new)
width = len(inputfile[0])
height = len(inputfile)
ispart1 = True

def near(lines, xo, yo):
	global ispart1
	global height

	count = 0
	for yc in range(-1, 2):
		for xc in range(-1, 2):
			if yc == 0 and xc == 0:
				continue
			x = xo + xc
			y = yo + yc
			while (y >= 0 and y < height and
				x >= 0 and x < width):
				if lines[y][x] == '#':
					count += 1
					break
				elif ispart1 or lines[y][x] == 'L':
					break
				x += xc
				y += yc
	return count

def solve():	
	global inputfile
	global ispart1
	global height
	lines = deepcopy(inputfile)

	change = 1
	while change:
		change = 0
		lines_copy = deepcopy(lines)
		for y in range(height):
			for x in range(width):
				if lines[y][x] == 'L' and near(lines, x, y) == 0:
					lines_copy[y][x] = '#'
					change = 1
				elif lines[y][x] == '#' and near(lines, x, y) >= (4 if ispart1 else 5):
					lines_copy[y][x] = 'L'
					change = 1
		lines = lines_copy
	res = 0
	for line in lines:
		res += line.count('#')
	return res

print(solve())
ispart1 = False
print(solve())
