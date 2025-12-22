import time

st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

inputList = []
with open(inputFile, "r") as i:
    for line in i:
        coords = tuple(map(int, line.rstrip("\n").split(",")))
        inputList.append(coords)


def buildFilledRanges(inputList):
    n = len(inputList)
    crossingsByY = {}

    for idx, (x1, y1) in enumerate(inputList):
        x2, y2 = inputList[(idx + 1) % n]

        if x1 == x2:
            yStart = min(y1, y2)
            yEnd = max(y1, y2)

            for y in range(yStart, yEnd):
                crossingsByY.setdefault(y, []).append(x1)

        elif y1 == y2:
            continue

    filledRanges = {}

    for y, xs in crossingsByY.items():
        xs.sort()
        ranges = []
        limit = len(xs) - (len(xs) % 2)
        for j in range(0, limit, 2):
            xL = xs[j]
            xR = xs[j + 1]
            if xL > xR:
                xL, xR = xR, xL
            ranges.append((xL, xR))
        if ranges:
            filledRanges[y] = ranges

    for idx, (x1, y1) in enumerate(inputList):
        x2, y2 = inputList[(idx + 1) % n]

        if y1 == y2:
            y = y1
            xL = min(x1, x2)
            xR = max(x1, x2)
            filledRanges.setdefault(y, []).append((xL, xR))

        elif x1 == x2:
            x = x1
            yStart = min(y1, y2)
            yEnd = max(y1, y2)
            for y in range(yStart, yEnd + 1):
                filledRanges.setdefault(y, []).append((x, x))

    for y, ranges in list(filledRanges.items()):
        ranges.sort()
        merged = []
        for a, b in ranges:
            if not merged or a > merged[-1][1] + 1:
                merged.append([a, b])
            else:
                merged[-1][1] = max(merged[-1][1], b)
        filledRanges[y] = [(a, b) for a, b in merged]

    return filledRanges

def isRectInside(filledRanges, xL, xR, yT, yB):
    for y in range(yT, yB + 1):
        ranges = filledRanges.get(y)
        if not ranges:
            return False

        ok = False
        for a, b in ranges:
            if a <= xL and b >= xR:
                ok = True
                break
            if a > xL:
                break
        if not ok:
            return False

    return True


def findMaxRectAreaFromInputCorners(inputList, filledRanges):
    n = len(inputList)
    maxArea = 0

    for i in range(n):
        x1, y1 = inputList[i]
        for j in range(i + 1, n):
            x2, y2 = inputList[j]

            if x1 == x2 or y1 == y2:
                continue

            xL = x1 if x1 < x2 else x2
            xR = x2 if x1 < x2 else x1
            yT = y1 if y1 < y2 else y2
            yB = y2 if y1 < y2 else y1

            area = (xR - xL + 1) * (yB - yT + 1)
            if area <= maxArea:
                continue

            if isRectInside(filledRanges, xL, xR, yT, yB):
                maxArea = area

    return maxArea


filledRanges = buildFilledRanges(inputList)
maxResult = findMaxRectAreaFromInputCorners(inputList, filledRanges)

print(maxResult)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")