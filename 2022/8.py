import sys

f = open(sys.argv[1], 'r')
file = f.read().splitlines()

def solve_dir(x, y, cx, cy, h):
	dist = 1
	x = x + cx
	y = y + cy
	while x >= 0 and y >= 0 and x < len(file[0]) and y < len(file):
		if ord(file[y][x]) >= h:
			break
		dist = dist + 1
		x = x + cx
		y = y + cy
	if x == -1 or y == -1 or x == len(file[0]) or y == len(file):
		return 1, dist - 1
	return 0, dist

def solve(x, y):
	edge = 0
	score = 1
	h = ord(file[y][x])
	a, b = solve_dir(x, y, -1, 0, h); edge = edge + a; score = score * b
	a, b = solve_dir(x, y,  1, 0, h); edge = edge + a; score = score * b
	a, b = solve_dir(x, y, 0, -1, h); edge = edge + a; score = score * b
	a, b = solve_dir(x, y, 0,  1, h); edge = edge + a; score = score * b
	return (1, 0)[edge == 0], score


part1 = 0
part2 = 0
for y in range(len(file)):
	for x in range(len(file[0])):
		tmp1, tmp2 = solve(x, y)
		part1 = part1 + tmp1
		part2 = max(part2, tmp2)
print("part1: " + str(part1))
print("part2: " + str(part2))
