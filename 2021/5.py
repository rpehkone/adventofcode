import fileinput

nums = []
for line in fileinput.input():
	row = []
	sides = line.split('->')
	values = sides[0].strip().split(',')
	row.append(int(values[0]))
	row.append(int(values[1]))
	values = sides[1].strip().split(',')
	row.append(int(values[0]))
	row.append(int(values[1]))
	nums.append(row)

flat = []
diag = []
w = 0
h = 0

def max3(a, b, c):
	return (max(max(a, b), c))

for line in nums:
	w = max3(line[0], line[2], w)
	h = max3(line[1], line[3], h)
	if line[0] == line[2] or line[1] == line[3]:
		flat.append(line)
	elif abs(line[0] - line[2]) == abs(line[1] - line[3]):
		diag.append(line)

#generate empty grid
grid = []
for i in range(h + 1):
	inner = []
	for j in range(w + 1):
		inner.append(0)
	grid.append(inner)

#draw flat lines
for line in flat:
	y = min(line[1], line[3])
	x = min(line[0], line[2])
	if line[1] == line[3]:
		while x <= max(line[0], line[2]):
			grid[y][x] = grid[y][x] + 1
			x += 1
	else:
		while y <= max(line[1], line[3]):
			grid[y][x] = grid[y][x] + 1
			y += 1

part1 = 0
for line in grid:
	for n in line:
		if n >= 2:
			part1 += 1
print("part1 = " + str(part1))

#draw diagonal lines
for line in diag:
	#always left to right
	if line[0] > line[2]:
		xtmp = line[0]
		ytmp = line[1]
		line[0] = line[2]
		line[1] = line[3]
		line[2] = xtmp
		line[3] = ytmp
	ydir = 1 if line[1] < line[3] else -1
	x = line[0]
	y = line[1]
	while x != line[2]:
		grid[y][x] += 1
		x += 1
		y += ydir
	grid[y][x] += 1

part2 = 0
for line in grid:
	for n in line:
		if n >= 2:
			part2 += 1

print("part2 = " + str(part2))
