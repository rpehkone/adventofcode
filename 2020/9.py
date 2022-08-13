import fileinput

nums = []
for line in fileinput.input():
	nums.append(int(line))

def solve_part1():
	i = 25
	while i < len(nums):
		n = nums[i]
		found = False
		for x in range(1, 26):
			for y in range(1, 26):
				if x != y and nums[i - x] + nums[i - y] == n:
					found = True
					break
		if not found:
			return nums[i]
		i += 1
	
def solve_part2(find):
	i = len(nums) - 1
	while i > 0:
		k = i
		count = 0
		while k > 0 and count < find:
			count += nums[k]
			k -= 1
		if k != i - 1 and count == find:
			weak = []
			k += 1
			while k <= i:
				weak.append(nums[k])
				k += 1
			weak.sort()
			return (weak[0] + weak[-1])
		i -= 1

part1 = solve_part1()
print(part1)
part2 = solve_part2(part1)
print(part2)
