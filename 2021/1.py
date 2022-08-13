import fileinput

num = []
for line in fileinput.input():
	num.append(int(line))

part2 = []
res = 0
for i in range(len(num) - 1):
	if num[i] < num[i + 1]:
		res += 1
	if i > 0:
		part2.append(num[i - 1] + num[i] + num[i + 1])
print(res)

res = 0
for i in range(len(part2) - 1):
	if part2[i] < part2[i + 1]:
		res += 1

print(res)
