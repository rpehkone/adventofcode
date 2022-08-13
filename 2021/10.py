import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)

part1 = 0
part2 = []
for line in lines:
	stack = ""
	i = 0
	for c in line:
		i += 1
		if c in "([{<":
			stack += c
		elif c == ')':
			if stack[-1:] == '(':
				stack = stack[:-1]
			else:
				part1 += 3
				break
		elif c == ']':
			if stack[-1:] == '[':
				stack = stack[:-1]
			else:
				part1 += 57
				break
		elif c == '}':
			if stack[-1:] == '{':
				stack = stack[:-1]
			else:
				part1 += 1197
				break
		elif c == '>':
			if stack[-1:] == '<':
				stack = stack[:-1]
			else:
				part1 += 25137
				break
	if i == len(line):
		stack = stack[::-1]
		score = 0
		for k in range(len(stack)):
			score = score * 5
			if stack[k] == '(':
				score += 1
			elif stack[k] == '[':
				score += 2
			elif stack[k] == '{':
				score += 3
			elif stack[k] == '<':
				score += 4
		part2.append(score)

print(part1)
part2 = sorted(part2)
print(part2[int(len(part2) / 2)])
