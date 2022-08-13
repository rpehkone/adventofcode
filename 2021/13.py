import fileinput

lines = []
splits = []
a = 0
for line in fileinput.input():
	line = line.strip()
	if line == '':
		a = 1
		continue
	if a:
		tmp = line.strip().split(' ')
		tmp = tmp[2].split('=')
		splits.append(tmp)
	else:
		lines.append(line.strip())

nums = []
maxy = 0
maxx = 0
for line in lines:
	tmp = line.split(',')
	tmp[0] = int(tmp[0])
	tmp[1] = int(tmp[1])
	nums.append(tmp)
	if tmp[0] > maxx:
		maxx = tmp[0]
	if tmp[1] > maxy:
		maxy = tmp[1]

maxx += 1
maxy += 1
area = []
for y in range(maxy):
	tmp  = []
	for x in range(maxx):
		tmp.append('.')
	area.append(tmp)
	
for n in nums:
	area[n[1]][n[0]] = 'x'

def foldx(x):
	global maxx
	global area
	mid = x - 1
	i = 0
	x += 1
	while x < maxx:
		for y in range(maxy):
			if area[y][x] == 'x':
				area[y][mid - i] = 'x'
		i += 1
		x += 1
	maxx = mid + 1

def foldy(y):
	global maxy
	global area
	mid = y - 1
	i = 0
	y += 1
	while y < maxy:
		for x in range(maxx):
			if area[y][x] == 'x':
				area[mid - i][x] = 'x'
		i += 1
		y += 1
	maxy = mid + 1

def count_part1():
	res = 0
	for y in range(maxy):
		for x in range(maxx):
			if area[y][x] == 'x':
				res += 1
	print(res)

part1 = 0
for split in splits:
	if split[0] == 'x':
		foldx(int(split[1]))
	else:
		foldy(int(split[1]))
	if not part1:
		part1 = 1
		count_part1()

for y in range(maxy):
	l = "".join(area[y][:maxx])
	print(l)
