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
        inputList.append(line.rstrip("\n"))

currentWayPoints = []
positionOfNoHitSplitters = []
for x, line in enumerate(inputList):
    for y, space in enumerate(line):
        if x == 0:
            if space == "S":
                currentWayPoints.append([x+1, y])
        if x%2 > 0:
            break
        if space == "^":
            currentPosition = [x, y]
            if [x-1, y] in currentWayPoints:
                currentWayPoints.remove([x-1, y])
                if y-1 >= 0 and [x+1, y-1] not in currentWayPoints:
                    currentWayPoints.append([x+1, y-1])
                if y+1 < len(line) and [x+1, y+1] not in currentWayPoints: 
                    currentWayPoints.append([x+1, y+1])
            else:
                positionOfNoHitSplitters.append([x, y])
        elif [x-1, y] in currentWayPoints:
            currentWayPoints.remove([x-1, y])
            currentWayPoints.append([x+1, y])
            
for noHitSplitter in positionOfNoHitSplitters:
    tmp = []
    for index, letter in enumerate(inputList[noHitSplitter[0]]):
        if index != noHitSplitter[1]:
            tmp.append(letter)
        else: 
            tmp.append(".")
    string = ''.join(tmp)
    inputList[noHitSplitter[0]] = string

amountOfPaths = []
for x, line in enumerate(inputList):
    for y, space in enumerate(line):
        if x == 0:
            if space == "S":
                amountOfPaths.append(1)  
            else:
                amountOfPaths.append(0)
        if x%2 > 0:
            break
        if space == "^":
            amountOfPaths[y-1] = amountOfPaths[y-1] + amountOfPaths[y]
            amountOfPaths[y+1] = amountOfPaths[y+1] + amountOfPaths[y]
            amountOfPaths[y] = 0

# too low: 1445
print(sum(amountOfPaths))

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")