import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()

part2 = False
def get_digit(i, line):
    char = line[i]
    if char.isdigit():
        return int(char)
    if part2:
        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for k, prefix in enumerate(nums):
            if line[i:].startswith(prefix):
                return k + 1
    return 0

def solve():
    res = 0
    for line in lines:
        line = line.strip()
        first = None
        last = None
        for i in range(len(line)):
            num = get_digit(i, line)
            if num != 0:
                last = str(num)
                if not first:
                    first = str(num)
        res += int(first + last)
    return res

print("part1:", solve())
part2 = True
print("part2:", solve())
