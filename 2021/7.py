import fileinput

nums = []
for line in fileinput.input():
	l = line.split(',')
	for n in l:
		nums.append(int(n))

nums.sort()

part1 = 0
median = nums[int(len(nums) / 2)]
for n in nums:
    part1 += abs(median - n)
print(part1)

part2 = 999999999
for i in range(len(nums)):
    fuel = 0
    for n in nums:
        diff = abs(nums[i] - n)
        fuel += int((diff * (diff + 1)) / 2)
    if fuel < part2:
        part2 = fuel
print(part2)
