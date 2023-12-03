import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
	lines[i] = line.strip()

def has_symbol_near(map, x, y, ispart2=False, excludes=False):
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
	if excludes:
		directions = [item for item in directions if item not in excludes]
	for dx, dy in directions:
		new_x, new_y = x + dx, y + dy
		if 0 <= new_x < len(map[0]) and 0 <= new_y < len(map):
			c = map[new_y][new_x]
			if ispart2 == 1:
				if c == '*':
					return [new_x, new_y]
			elif ispart2 == 2:
				if c.isdigit():
					return [new_x, new_y]
			else:
				if not c.isdigit() and c != ".":
					return True
	return False

part1 = 0
part2 = 0

def get_int_from_coords(x, y):
	x_start = x
	while x_start >= 0 and lines[y][x_start].isdigit():
		x_start -= 1
	x_stop = x
	while x_stop < len(lines[0]) and lines[y][x_stop].isdigit():
		x_stop += 1
	return int(lines[y][x_start + 1:x_stop])

#loop num1 chars
#find *
#find num2
seen_gears = []
def solve_part2(x_start, x_stop, y):
	global part2
	x = x_start
	while x < x_stop:
		gear = has_symbol_near(lines, x, y, ispart2=1)
		if gear and gear not in seen_gears:
			num1_coords = [(x - gear[0], y - gear[1]) for x in range(x_start, x_stop)]#num1 relative to gear coords
			num1_coords = [coord for coord in num1_coords if all(num in [-1, 0, 1] for num in coord)]#remove not adjacent to gear

			num2pos = has_symbol_near(lines, gear[0], gear[1], ispart2=2, excludes=num1_coords)
			if num2pos:
				seen_gears.append(gear)
				num1 = int(lines[y][x_start:x_stop])
				num2 = get_int_from_coords(num2pos[0], num2pos[1])
				part2 += num1 * num2
				return
		x += 1

for y, line in enumerate(lines):
	i = 0
	while i < len(line):
		start = i
		while i < len(line) and line[i].isdigit():
			i += 1
		if line[start].isdigit():
			x = start
			while x < i:
				if has_symbol_near(lines, x, y):
					part1 += int(line[start:i])
					break
				x += 1
			solve_part2(start, i, y)
		while i < len(line) and not line[i].isdigit():
			i += 1

print("part1:", part1)
print("part2:", part2)
