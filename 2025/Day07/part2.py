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

positionOfSplitters = []
currentWayPoints = []
for x, line in enumerate(inputList):
    for y, space in enumerate(line):
        if x == 0:
            if space == "S":
                currentWayPoints.append([x+1, y])
                break
        if x%2 > 0:
            break
        if space == "^":
            currentPosition = [x, y]
            if [x-1, y] in currentWayPoints:
                positionOfSplitters.append(currentPosition)
                currentWayPoints.remove([x-1, y])
                if y-1 >= 0 and [x+1, y-1] not in currentWayPoints:
                    currentWayPoints.append([x+1, y-1])
                if y+1 < len(line) and [x+1, y+1] not in currentWayPoints: 
                    currentWayPoints.append([x+1, y+1])
        elif [x-1, y] in currentWayPoints:
            currentWayPoints.remove([x-1, y])
            currentWayPoints.append([x+1, y])
         
            
                    


# too low: 1445
print(len(positionOfSplitters))

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")