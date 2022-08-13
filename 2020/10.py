import fileinput

asd = []
for line in fileinput.input():
	asd.append(int(line))

asd.append(0)
asd.append(max(asd) + 3)
asd.sort()
diff1 = 0
diff2 = 0
size = len(asd)
for n in range(size - 1):
	d = asd[n + 1] - asd[n]
	if d == 1:
		diff1 += 1
	if d == 3:
		diff2 += 1
print(diff1 * diff2)

seen = {}
def part2(n):
	if n == size - 1:
		return 1
	if n in seen:
		return seen[n]
	res = 0
	for m in range(n + 1, size):
		if asd[m] - asd[n] <= 3:
			res += part2(m)
	seen[n] = res
	return res
print(part2(0))
