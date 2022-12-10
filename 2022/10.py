import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)

x = 1
cycles = 0
part1 = 0

def check_signal():
	global part1
	tests = [20, 60, 100, 140, 180, 220]
	if cycles in tests:
		strenght = cycles * x
		part1 = part1 + strenght

def crt():
	n = cycles % 40
	if not n:
		print()
	else:
		c = '#' if n in range(x - 1, x + 2) else '.'
		print(c, end='')

def cpu_tick():
	global cycles
	crt()
	cycles += 1
	check_signal()

for line in lines:
	line = line.strip()
	words = line.split(' ')
	if words[0] == "noop":
		cpu_tick()
	elif words[0] == "addx":
		cpu_tick()
		cpu_tick()
		x += int(words[1])

print()
print("part1: " + str(part1))
