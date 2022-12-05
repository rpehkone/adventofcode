from copy import deepcopy
import sys


f = open(sys.argv[1], 'r')
file = f.read().split('\n\n')
initial = file[0].split('\n')
moves = file[1].split('\n')
moves = [i for i in moves if i]

array = [None] * 100
for i in range(100):
	array[i] = []

for i in range(len(initial[0]) - 1):
	for k in range(len(initial)):
		if initial[k][i + 1] == ']':
			array[(int((i - 1) / 4))].append(initial[k][i])
for i in range(100):
	array[i].reverse()

def solve(moves, array, ispart2):
	for move in moves:
		move = move.split(' ')
		for _ in reversed(range(int(move[1]))):
			k = 1
			if ispart2:
				k = _ + 1
			char = array[int(move[3]) - 1][-k]
			del array[int(move[3]) - 1][-k]
			array[int(move[5]) - 1].append(char[0])
	res = ''
	for i in range(100):
		char = array[i][-1:]
		if char:
			res = res + char[0]
	return res

stack = deepcopy(array)
print("part1: " + solve(moves, stack, False))
print("part2: " + solve(moves, array, True))
