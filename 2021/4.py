import fileinput

lines = []
for line in fileinput.input():
	lines.append(line.strip())

nums = lines[0].split(',')
lines = lines[2:]

boards = []
board = []

for line in lines:
	if not line:
		boards.append(board)
		board = []
	else:
		board.append(line.split())
boards.append(board)
board = []

seen = []#boards that have won
p1found = False

for n in nums:
	for board in boards:
		for y in range(len(board[0])):
			for x in range(len(board[0])):
				if board[y][x] == n:
					board[y][x] = 'x'
	for i, board in enumerate(boards):
		for y in range(len(board[0])):
			c = 0
			for x in range(len(board[0])):
				if board[y][x] == 'x':
					c += 1
			if c == len(board[0]) and i not in seen:
				seen.append(i)
		for x in range(len(board[0])):
			c = 0
			for y in range(len(board[0])):
				if board[y][x] == 'x':
					c += 1
			if c == len(board[0]) and i not in seen:
				seen.append(i)
		if len(seen) == len(boards) or len(seen) == 1 and not p1found:
			res = 0
			for dy in range(len(board[0])):
				for dx in range(len(board[0])):
					if board[dy][dx] != 'x':
						res += int(board[dy][dx])
			if (len(seen) == 1):
				print("part1 = " + str(res * int(n)))
				p1found = True
			else:
				print("part2 = " + str(res * int(n)))
				exit()
