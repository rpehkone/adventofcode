import fileinput

nums = []
map = []
for line in fileinput.input():
	tmp = []
	maptmp = []
	line = line.strip()
	for c in line:
		tmp.append(int(c))
		maptmp.append(int(0))
	nums.append(tmp)
	map.append(maptmp)

def flood(x, y):
	nums[y][x] += 1
	if nums[y][x] <= 9:
		return
	if map[y][x] == 'x':
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
	if x < xmax and y < ymax:
		flood(x + 1, y + 1)
	if x > 0 and y < ymax:
		flood(x - 1, y + 1)
	if x < xmax and y > 0:
		flood(x + 1, y - 1)
	if x > 0 and y > 0:
		flood(x - 1, y - 1)

steps = 0
part1 = 0
while True:
	for y in range(len(nums)):
		for x in range(len(nums[0])):
			nums[y][x] += 1
	for y in range(len(nums)):
		for x in range(len(nums[0])):
			if nums[y][x] > 9:
				flood(x, y)
	
	part2 = 0
	for y in range(len(nums)):
		for x in range(len(nums[0])):
			map[y][x] = 0
			if nums[y][x] > 9:
				part1 += 1
				part2 += 1
				nums[y][x] = 0
	steps += 1
	if steps == 100:
		print(part1)
	if part2 == len(nums) * len(nums[0]):
		print(steps)
		exit()