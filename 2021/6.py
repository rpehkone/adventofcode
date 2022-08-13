import fileinput

nums = []
for line in fileinput.input():
	l = line.split(',')
	for n in l:
		nums.append(int(n))

seen = []
def getfish(n, days):
	for s in seen:
		if s[0] == n and s[1] == days:
			return s[2]
	og = days
	fish = []
	fish.append(n)
	actual = days
	if days > 100:
		actual = 100
		days -= 100
	for i in range(actual):
		for k in range(len(fish)):
			fish[k] -= 1
			if fish[k] == -1:
				fish.append(8)
				fish[k] = 6
	res = 0
	if actual == 100:
		for f in range(len(fish)):
			res += getfish(fish[f], days)
	else:
		res = len(fish)
	t = (n, og, res)
	seen.append(t)
	return(res)

def solve(iterations):
	res = 0
	for n in nums:
		res += getfish(n, iterations)
	return res

print("part1 = " + str(solve(80)))
print("part2 = " + str(solve(256)))