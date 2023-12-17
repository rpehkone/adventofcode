import os, strutils
import options

var lines: seq[string] = @[]
let inputFile = paramStr(1)

for line in inputFile.lines:
    lines.add(line.strip())

var part2 = false

proc getDigit(i: int, line: string): int =
    let char = line[i]
    if char.isDigit():
        return parseInt($char)
    if part2:
        let nums = @["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        for idx, prefix in nums:
            if line.substr(i).startsWith(prefix):
                return idx + 1
    return 0

proc solve(): int =
    var result = 0
    for getline in lines:
        let line = getline.strip()
        var first: Option[string] = none(string)
        var last: Option[string] = none(string)
        for i in 0 ..< line.len:
            let num = getDigit(i, line)
            if num != 0:
                last = some($num)
                if first.isNone:
                    first = some($num)
        result += parseInt($first.get & $last.get)
    result

echo "part1: ", solve()
part2 = true
echo "part2: ", solve()
