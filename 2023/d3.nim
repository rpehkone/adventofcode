import os, strutils, sequtils

let inputFile = paramStr(1)
var lines = readFile(inputFile).splitLines()

for i in 0 ..< lines.len:
    lines[i] = lines[i].strip()

proc hasSymbolNear(map: seq[string], x: int, y: int, ispart2: int, excludes: seq[(int, int)]): (bool, int, int) =
    var directions1 = toSeq([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)])
    var directions: seq[(int, int)] = @[]
    for dir in directions1:
        if not (dir in excludes):
            directions.add(dir)

    for direction in directions:
        let (newX, newY) = (x + direction[0], y + direction[1])
        if newX >= 0 and newX < map[0].len and newY >= 0 and newY < map.len:
            let c = map[newY][newX]
            if ispart2 == 0:
                if not c.isDigit and c != '.':
                    return (true, 0, 0)
            if ispart2 == 1:
                if c == '*':
                    return (true, newX, newY)
            if ispart2 == 2:
                if c.isDigit() and c != '.':
                    return (true, newX, newY)
    return (false, 0, 0)

proc getIntFromCoords(x, y: int): int =
    var xStart = x
    while xStart >= 0 and lines[y][xStart].isDigit:
        dec(xStart)
    var xStop = x
    while xStop < lines[y].len and lines[y][xStop].isDigit:
        inc(xStop)
    return parseInt(lines[y][xStart + 1 ..< xStop])

var part1 = 0
var part2 = 0

#loop num1 chars
#find *
#find num2
var seenGears: seq[(int, int)]
proc solvePart2(xStart, xStop, y: int) =
    var dummySeq: seq[(int, int)] = @[]
    var x = xStart
    while x < xStop:
        let (hasSym2, gearx, geary) = hasSymbolNear(lines, x, y, 1, dummySeq)
        if hasSym2 and not ((gearx, geary) in seenGears):
            var num1Coords: seq[(int, int)]
            for x in xStart ..< xStop:
                let allowed = [-1, 0, 1]
                let tmpX = x - gearx
                let tmpY = y - geary
                if tmpX in allowed and tmpY in allowed:
                    num1Coords.add((x - gearx, y - geary))
            let (hasSym3, num2x, num2y) = hasSymbolNear(lines, gearx, geary, 2, num1Coords)
            if hasSym3:
                seenGears.add((gearx, geary))
                let num1 = parseInt(lines[y][xStart ..< xStop])
                let num2 = getIntFromCoords(num2x, num2y)
                part2 += num1 * num2
                return
        inc(x)

for y in 0 ..< lines.len:
    var i = 0
    while i < lines[y].len:
        let start = i
        while i < lines[y].len and lines[y][i].isDigit:
            inc(i)
        if lines[y][start].isDigit:
            var x = start
            while x < i:
                var dummySeq: seq[(int, int)] = @[]
                let (hasSym, newx, newy) = hasSymbolNear(lines, x, y, 0, dummySeq)
                if hasSym:
                    part1 += getIntFromCoords(start, y)
                    break
                inc(x)
            solvePart2(start, i, y)
        while i < lines[y].len and not lines[y][i].isDigit:
            inc(i)

echo "part1: ", part1
echo "part2: ", part2
