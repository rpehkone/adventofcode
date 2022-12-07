import sys

def draw_filesystem(d, indent=0):
	for key, value in d.items():
		if isinstance(value, dict):
			print('    ' * indent + str(key))
			draw_filesystem(value, indent + 1)
		else:
			print('    ' * (indent + 0) + str(key) + " : " + str(value))

def count_sizes(d, indent=0):
	tmp = 0
	for key, value in d.items():
		if isinstance(value, dict):
			tmp += count_sizes(value, indent+1)
		else:
			tmp += int(value)
	d["directory_size"] = tmp
	return tmp

def build_filesystem(file):
	fs = {}#filesystem
	wd = fs#working directory
	path = []#path of working directory
	i = 1
	isls = False

	while i < len(file):
		w = file[i].split(' ')
		if w[0] == '$':
			isls = False
		if isls:
			if w[0] == "dir":
				wd[w[1]] = {}
			else:
				wd[w[1]] = w[0]
		if w[0] == '$':
			if w[1] == "ls":
				isls = True
			elif w[1] == "cd":
				if w[2] == "..":
					path.pop()
					wd = fs
					for c in path:
						wd = wd[c]
				else:
					path.append(w[2])
					wd = wd[w[2]]
		i = i + 1
	return fs

def part1(d, indent=0):
	tmp = 0
	for key, value in d.items():
		if isinstance(value, dict):
			tmp += part1(value, indent+1)
		if key == "directory_size" and int(value) <= 100000:
			tmp += int(value)
	return tmp

def part2(d, max, smallest):
	for key, value in d.items():
		if isinstance(value, dict):
			smallest = part2(value, max, smallest)
		if key == "directory_size" and int(value) >= max and int(value) < smallest:
			smallest = int(value)
	return smallest

f = open(sys.argv[1], 'r')
file = f.read().splitlines()

fs = build_filesystem(file)
fs_size = count_sizes(fs)
draw_filesystem(fs)
print()

print("part1: " + str(part1(fs)))
freespace = 70000000 - fs_size
need_to_free = 30000000 - freespace
print("part2: " + str(part2(fs, need_to_free, 9999999999)))
