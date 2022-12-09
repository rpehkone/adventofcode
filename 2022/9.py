from copy import deepcopy
import sys

f = open(sys.argv[1], 'r')
file = f.read().splitlines()

def draw(map, size):
	for y in reversed(range(size)):
		for x in range(size):
			if [x, -y] in map:
				print('# ', end='')
			else:
				print('. ', end='')
		print()

def solve(joint_amount):
	tail_seen = []
	tail_seen.append([0, 0])
	joint_pos = []
	for _ in range(joint_amount):
		joint_pos.append([0, 0])
	for s in file:
		s = s.strip()
		w = s.split()
		change = [0, 0]
		if w[0]   == 'R':
			change[0] = 1
		elif w[0] == 'L':
			change[0] = -1
		elif w[0] == 'U':
			change[1] = -1
		elif w[0] == 'D':
			change[1] = 1

		for _ in range(int(w[1])):
			joint_pos[0][0] += change[0]
			joint_pos[0][1] += change[1]
			for n in range(1, joint_amount):
				movex = joint_pos[n - 1][0] - joint_pos[n][0]
				movey = joint_pos[n - 1][1] - joint_pos[n][1]
				if abs(movex) > 1 or abs(movey) > 1:
					new = deepcopy(joint_pos[n])
					if movex > 0:
						new[0] += 1
					elif movex < 0:
						new[0] -= 1
					if movey > 0:
						new[1] += 1
					elif movey < 0:
						new[1] -= 1
					joint_pos[n] = new
			if joint_pos[-1] not in tail_seen:
				tail_seen.append(joint_pos[-1])
	# draw(tail_seen, 6)
	return len(tail_seen)

print("part1: " + str(solve(2)))
print("part2: " + str(solve(10)))
