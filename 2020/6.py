import fileinput
from collections import Counter

def solve_part2(clist, group):
	res = 0
	for c in clist:
		count = 0
		for line in group:
			if c in line:
				count += 1
		if count == len(group):
			res += 1
	return res
		
def charlist(group):
	used = []
	for line in group:
		for c in line:
			used.append(c)
	clist = Counter(used).keys()
	clist = list(clist)
	clist.remove('\n')
	return clist

lines = []
for line in fileinput.input():
	lines.append(line)

part1 = 0
part2 = 0
group = []
def solve():
	global group
	global part1
	global part2
	clist = charlist(group)
	part1 += len(clist)
	part2 += solve_part2(clist, group)
	group = []

for line in lines:
	if line[0] == '\n':
		solve()
	else:
		group.append(line)
solve()
print(part1)
print(part2)
