import fileinput

lines = []
for line in fileinput.input():
	lines.append(line.strip())

enhance = lines[0]
grid = lines[2:]

startx = len(grid[0])
stopx = len(grid[0]) * 2
starty = len(grid)
stopy = len(grid) * 2
res = []
for y in range(len(grid) * 3):
	tmp = []
	for x in range(len(grid[0]) * 3):
		tmp.append('.')
	res.append(tmp)

for y in range(len(grid)):
	for x in range(len(grid[0])):
		res[y + len(grid)][x + len(grid[0])] = grid[y][x]
grid = res

def getpixel(x, y, img):
	global enhance
	str = img[y - 1][x - 1:x + 2]
	str += img[y - 0][x - 1:x + 2]
	str += img[y + 1][x - 1:x + 2]
	str = "".join(str)
	str = str.replace('#', '1')
	str = str.replace('.', '0')
	return enhance[int(str, 2)]

iii = 0
def solve(img):
	global iii
	iii += 1
	global startx
	global stopx
	global starty
	global stopy
	startx -= 1
	starty -= 1
	stopx += 1
	stopy += 1
	res = []
	for y in range(len(img)):
		tmp = []
		for x in range(len(img[0])):
			if iii % 2:
				tmp.append(enhance[0])
			else:
				tmp.append('.')
		res.append(tmp)
	y = starty
	while y < stopy:
		x = startx
		while x < stopx:
			res[y][x] = getpixel(x, y, img)
			x += 1
		y += 1
	return (res)


def countlit(grid):
	lit = 0
	for line in grid:
		for c in line:
			if c == '#':
				lit += 1
	return lit

grid = solve(grid)
grid = solve(grid)
print("part1 = " + str(countlit(grid)))

for i in range(50 - 2):
	grid = solve(grid)
print("part2 = " + str(countlit(grid)))
