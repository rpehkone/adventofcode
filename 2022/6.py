from collections import Counter
import sys

f = open(sys.argv[1], 'r')
file = f.read()

def solve(n):
	for i, c in enumerate(file):
		arr = file[i:i + n]
		c = Counter(arr)
		if len(c) == len(arr) == n:
			return i + n

print("part1: " + str(solve(4)))
print("part2: " + str(solve(14)))
