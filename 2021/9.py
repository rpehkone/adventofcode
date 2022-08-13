import fileinput

nums = []
map = []
for line in fileinput.input():
	tmp = []
	maptmp = []
	line = line.strip()
	for c in line:
		tmp.append(int(c))
		maptmp.append(0)
	nums.append(tmp)
	map.append(maptmp)

part1 = 0
for y in range(len(nums)):
	for x in range(len(nums[0])):
		c = nums[y][x]
		xmax = len(nums[0]) - 1
		ymax = len(nums) - 1
		if	(x == 0		or c < nums[y][x - 1]) and\
			(x == xmax	or c < nums[y][x + 1]) and\
			(y == 0		or c < nums[y - 1][x]) and\
			(y == ymax	or c < nums[y + 1][x]):
				part1 += c + 1
print(part1)

#part2
def flood(x, y):
	c = nums[y][x]
	if c == 9 or map[y][x] == 'x':
		return
	map[y][x] = 'x'
	xmax = len(nums[0]) - 1
	ymax = len(nums) - 1
	if y > 0:
		flood(x, y - 1)
	if y < ymax:
		flood(x, y + 1)
	if x > 0:
		flood(x - 1, y)
	if x < xmax:
		flood(x + 1, y)

sizes = []
for y in range(len(nums)):
	for x in range(len(nums[0])):
		c = nums[y][x]
		if c == 9:
			continue
		flood(x, y)
		s = 0
		firstx = -1
		firsty = -1
		for dy in range(len(nums)):		#count surface area
			for dx in range(len(nums[0])):
				if map[dy][dx] == 'x':
					if firstx == -1 and firsty == -1:
						firstx = dx			#save location to remove duplicates
						firsty = dy
					s += 1
		toup = (s, firstx, firsty)
		sizes.append(toup)
		for dy in range(len(nums)):		#reset flood fill map
			for dx in range(len(nums[0])):
				map[dy][dx] = '0'
sizes = list(dict.fromkeys(sizes))
sizes = sorted(sizes)
sizes = list(reversed(sizes))
print(sizes[0][0] * sizes[1][0] * sizes[2][0])
