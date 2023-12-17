import os, strutils, sequtils

let inputFile = paramStr(1)
var lines = readFile(inputFile).splitLines()
lines = lines.filter(proc(line: string): bool = line.len > 0)

var part1 = 0
var part2 = 0

for line in lines:
    let parts = line.split(":")
    let gameID = (parts[0].split(" ")[1]).parseInt
    let game = parts[1].strip().replace(";", ",").split(",")

    var r = 0
    var g = 0
    var b = 0
    var possible = true

    for set in game:
        let elements = set.strip().split()
        let n = elements[0].parseInt

        if "red" in set:
            if n > 12:
                possible = false
            r = max(r, n)
        elif "green" in set:
            if n > 13:
                possible = false
            g = max(g, n)
        elif "blue" in set:
            if n > 14:
                possible = false
            b = max(b, n)

    if possible:
        part1 += gameID
    part2 += r * g * b

echo "part1: ", part1
echo "part2: ", part2
