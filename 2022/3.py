import fileinput

lines = []
for line in fileinput.input():
	lines.append(line.strip())

res = 0
for line in lines:
	left = line[:int(len(line) / 2)]
	right = line[int(len(line) / 2):]
	for k in range(len(left)):
		if left[k] in right:
			val = left[k]
			if val >= 'A' and val <= 'Z':
				val = ord(val) - ord('A') + 27
			else:
				val = ord(val) - ord('a') + 1
			res += val
			break
print("part1: " + str(res))


res = 0
for i in range(int(len(lines) / 3)):
	words = lines[i * 3:i * 3 + 3]
	for k in range(len(words[0])):
		if words[0][k] in words[1] and words[0][k] in words[2]:
			val = words[0][k]
			if val >= 'A' and val <= 'Z':
				val = ord(val) - ord('A') + 27
			else:
				val = ord(val) - ord('a') + 1
			res += val
			break

print("part2: " + str(res))
