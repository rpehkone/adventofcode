import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)

def solve(x, y, ispart1):
	p2x = 0
	p2y = 0
	dire = 1
	for line in lines:
		c = line[0]
		n = int(line[1:])
		if c == 'N':
			y += n
		elif c == 'S':
			y -= n
		elif c == 'E':
			x += n
		elif c == 'W':
			x -= n
		elif c == 'F':
			if ispart1:
				if dire == 0:
					y += n
				elif dire == 1:
					x += n
				elif dire == 2:
					y -= n
				elif dire == 3:
					x -= n
			else:
				for i in range(n):
					p2x += x
					p2y += y
		elif c == 'R':
			for i in range(int(n / 90)):
				if ispart1:
					dire = (dire + 1) % 4
				else:
					tmp = x
					x = y
					y = tmp * -1
		elif c == 'L':
			for i in range(int(n / 90)):
				if ispart1:
					dire = (dire - 1) % 4
				else:
					tmp = x
					x = y * -1
					y = tmp
	if ispart1:
		return abs(x) + abs(y)
	else:
		return abs(p2x) + abs(p2y)

print(solve(0, 0, True))
print(solve(10, 1, False))
