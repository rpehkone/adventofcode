#!/usr/bin/python3
from copy import deepcopy
import sys

f = open(sys.argv[1], 'r')
file = f.read().split('\n\n')

start_inventory = []
tests = []
for n, b in enumerate(file):
	monkey = b.split('\n')
	items_c = monkey[1].split(':')[1].split(',')
	test = int(monkey[3].split('by')[1])
	tests.append(test)
	items = []
	for item in items_c:
		items.append(int(item))
	start_inventory.append(items)
common_mul = 1
for n in tests:
	common_mul = common_mul * n

def solve(inventory, iterations, ispart2):
	res = [0] * len(inventory)
	for round in range(iterations):
		for n, b in enumerate(file):
			monkey = b.split('\n')
			op = monkey[2].split('=')[1]
			iftrue = int(monkey[4].split('monkey')[1])
			iffalse = int(monkey[5].split('monkey')[1])
			for item in inventory[n]:
				res[n] += 1
				old = item
				new = eval(op)
				if ispart2:
					new %= common_mul
				else:
					new /= 3
				if new % tests[n] == 0:
					inventory[iftrue].append(new)
				else:
					inventory[iffalse].append(new)
			inventory[n] = []
	res.sort()
	return res[-1] * res[-2]

print("part1: " + str(solve(deepcopy(start_inventory), 20, False)))
print("part2: " + str(solve(start_inventory, 10000, True)))
