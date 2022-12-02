import sys

f = open(sys.argv[1], 'r', encoding = "utf-16")
file = f.read().splitlines()

def solve(file, is_part2):
	res = 0
	for line in file:
		words = line.split()
		words[0] = ord(words[0]) - 65 + 1
		words[1] = ord(words[1]) - 88 + 1

		if is_part2:
			rot = [3, 1, 2]
			if words[1] == 1:
				words[1] = rot[words[0] - 1]
			elif words[1] == 2:
				words[1] = words[0]
			elif words[1] == 3:
				words[1] = words[0] % 3 + 1

		win = [2, 3, 1]
		if words[1] == win[words[0] - 1]:
			res = res + 6
		if words[0] == words[1]:#draw
			res = res + 3
		res = res + words[1]
	return (res)

print("part1: " + str(solve(file, False)))
print("part2: " + str(solve(file, True)))
