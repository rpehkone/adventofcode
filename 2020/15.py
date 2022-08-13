import fileinput

nums = []
for line in fileinput.input():
	line = line.rstrip()
	line = line.split(',')
	for n in line:
		nums.append(int(n))

seen = {}
for i in range(len(nums) - 1):
	seen[nums[i]] = i

def solve(nums, seen, find):
	while len(nums) < find:
		last2 = seen.get(nums[-1], -1) + 1
		seen[nums[-1]] = len(nums) - 1
		nums.append(len(nums) - last2 if last2 else 0)
	return nums[-1]

print(solve(nums, seen, 2020))
print(solve(nums, seen, 30000000))
