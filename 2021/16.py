import fileinput
import math

message = ""
for line in fileinput.input():
	line = line.strip()
	for c in line:
		tmp = int(c, 16)
		tmp = bin(tmp)
		tmp = str(tmp)
		tmp = tmp[2:]
		tmp = tmp.rjust(4, '0')
		message += tmp

i = 0
def bitmatch(test):
	global message
	global i
	for k in range(len(test)):
		if message[i + k] != test[k]:
			i += len(test)
			return False
	i += len(test)
	return True

def getint(lenght):
	global message
	global i
	res = message[i:i + lenght]
	i += lenght
	return int(int(res, 2))

def getliteral():
	global i
	num = ""
	get = message[i:i + 5]
	num += get[1:]
	i += 5
	while get[0] != '0':
		get = message[i:i + 5]
		num += get[1:]
		i += 5
	return(int(int(num, 2)))


part1 = 0
def solve(depth):
	debug = False
	global message
	global i
	global part1
	ver = getint(3)
	type = getint(3)
	part1 += ver

	if type == 4:
		n = getliteral()
		if debug:
			print("    " * depth + "lit " + str(n) + " v" + str(ver) + " t" + str(type))
		return (n)
	else:
		subs = []
		label = getint(1)
		if label == 0:
			lenght = getint(15)
			if debug:
				print("    " * depth + "opr v" + str(ver) + " t" + str(type) + " l" + str(label) + " bits " + str(lenght))
			tmp = i
			while i < tmp + lenght - 6:
				n = solve(depth + 1)
				subs.append(n)
			i = tmp
			i += lenght
		else:
			lenght = getint(11)
			if debug:
				print("    " * depth + "opr v" + str(ver) + " t" + str(type) + " l" + str(label) + " subs " + str(lenght))
			for k in range(lenght):
				n = solve(depth + 1)
				subs.append(n)
		if type == 0:
			return (sum(subs))
		elif type == 1:
			return (math.prod(subs))
		elif type == 2:
			return (min(subs))
		elif type == 3:
			return (max(subs))
		elif type == 5:
			return (subs[0] > subs[1])
		elif type == 6:
			return (subs[0] < subs[1])
		elif type == 7:
			return (subs[0] == subs[1])

part2 = solve(0)
print(part1)
print(part2)
