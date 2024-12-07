import time
import copy
st = time.process_time()
tmp = []
mapStruktur = []

# Aufbau Map wobei X die senkrechte Koordinate ist und Y die Waagerechte
#       Y  0    1    2    3    4    5    6    7    8    9 
#  X
#  0     ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.']
#  1     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#']
#  2     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#  3     ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.']
#  4     ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.']
#  5     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#  6     ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.']
#  7     ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.']
#  8     ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#  9     ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
# 

with open("input/input.txt", 'r') as file:
    for line in file:
        for letter in line:
            if not letter == "\n":
                tmp.append(letter)
        mapStruktur.append(tmp)
        tmp = []

mapClean = copy.deepcopy(mapStruktur)

def getStartingPositionAndChar():
    # get starting position
    for xCoord in range(len(mapStruktur) -1):
        for yCoord, char in enumerate(mapStruktur[xCoord]):
            if char == "." or char == "#" or char == "O":
                continue
            return xCoord, yCoord, char

def checkCurrentPosition(currentPosition):
    if currentPosition[0] < 0 or currentPosition[0] > len(mapStruktur)-1:
        return False
    if currentPosition[1] < 0 or currentPosition[1] > len(mapStruktur[currentPosition[1]])-1:
        return False
    return True

def moveUp(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X"
    try:
        nextPosition = [currentPosition[0] - 1, currentPosition[1]]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#" or mapStruktur[nextPosition[0]][nextPosition[1]] == "O":
            if mapStruktur[currentPosition[0]][currentPosition[1]+1] == "O":
                nextPosition = [currentPosition[0]+1, currentPosition[1]]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "v"
            else:
                nextPosition = [currentPosition[0], currentPosition[1]+1]
                mapStruktur[nextPosition[0]][nextPosition[1]] = ">"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = "^"
        return nextPosition
    except IndexError:
        return currentPosition
        
def moveRight(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X"
    try:
        nextPosition = [currentPosition[0], currentPosition[1]+1]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#" or mapStruktur[nextPosition[0]][nextPosition[1]] == "O":
            if mapStruktur[currentPosition[0]+1][currentPosition[1]] == "O":
                nextPosition = [currentPosition[0], currentPosition[1]-1]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "<"
            else:
                nextPosition = [currentPosition[0]+1, currentPosition[1]]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "v"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = ">"
        return nextPosition
    except IndexError:
        return currentPosition

def moveDown(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X" 
    try:
        nextPosition = [currentPosition[0]+1, currentPosition[1]]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#" or mapStruktur[nextPosition[0]][nextPosition[1]] == "O":
            if mapStruktur[currentPosition[0]][currentPosition[1]-1] == "O":
                nextPosition = [currentPosition[0]-1, currentPosition[1]]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "^"
            else:
                nextPosition = [currentPosition[0], currentPosition[1]-1]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "<"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = "v"
        return nextPosition
    except IndexError:
        return currentPosition

def moveLeft(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X"
    try:
        nextPosition = [currentPosition[0], currentPosition[1]-1]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#" or mapStruktur[nextPosition[0]][nextPosition[1]] == "O":
            if mapStruktur[currentPosition[0]-1][currentPosition[1]] == "O":
                nextPosition = [currentPosition[0], currentPosition[1]+1]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "v"
            else:
                nextPosition = [currentPosition[0]-1, currentPosition[1]]
                mapStruktur[nextPosition[0]][nextPosition[1]] = "^"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = "<"
        return nextPosition
    except IndexError:
        return currentPosition

def checkWay():
    xCoordStart, yCoordStart, char = getStartingPositionAndChar()
    currentPosition = [xCoordStart, yCoordStart]
    cl = False
    # cnt = 0
    way = []
    first = []
    while True:
        if "timer" in globals() and time.time() > timer + 120:
            return True
        if not checkCurrentPosition(currentPosition):
            break
        if cl:
            i = way.index(first)
            match char:
                case "^":
                    nextPos = [first[0]-1,first[1]]
                    
                case "<":
                    nextPos = [first[0], first[1]-1]
                    
                case ">":
                    nextPos = [first[0], first[1]+1]
                    
                case "v":
                    nextPos = [first[0]+1, first[1]]
                    
            if nextPos == way[i+1]:
                return True
            else:
                cl = False
                match char:
                    case "^":
                        way.pop(way.index(currentPosition))
                        # cnt += 1
                        way.append(currentPosition)
                        currentPosition = moveUp(currentPosition)
                        char = mapStruktur[currentPosition[0]][currentPosition[1]]
                    case "<":
                        way.pop(way.index(currentPosition))
                        # cnt += 1
                        way.append(currentPosition)
                        currentPosition = moveLeft(currentPosition)
                        char = mapStruktur[currentPosition[0]][currentPosition[1]]
                    case ">":
                        way.pop(way.index(currentPosition))
                        # cnt += 1
                        way.append(currentPosition)
                        currentPosition = moveRight(currentPosition)
                        char = mapStruktur[currentPosition[0]][currentPosition[1]]
                    case "v":
                        way.pop(way.index(currentPosition))
                        # cnt += 1
                        way.append(currentPosition)
                        currentPosition = moveDown(currentPosition)
                        char = mapStruktur[currentPosition[0]][currentPosition[1]]
                continue

        if currentPosition in way:
            cl = True
            first = currentPosition
            continue

        if char == "^":
            way.append(currentPosition)
            currentPosition = moveUp(currentPosition)
            char = mapStruktur[currentPosition[0]][currentPosition[1]]
        if char == ">":
            way.append(currentPosition)
            currentPosition = moveRight(currentPosition)
            char = mapStruktur[currentPosition[0]][currentPosition[1]]
        if char == "v":
            way.append(currentPosition)
            currentPosition = moveDown(currentPosition)
            char = mapStruktur[currentPosition[0]][currentPosition[1]]
        if char == "<":
            way.append(currentPosition)
            currentPosition = moveLeft(currentPosition)
            char = mapStruktur[currentPosition[0]][currentPosition[1]]
        if char == "X":
            break
    return False


checkWay()
possiblePos = set()
for xPos, line in enumerate(mapStruktur):
    for yPos, letter in enumerate(line):
        if letter == "X":
            possiblePos.add((xPos, yPos))

# print(possiblePos)
counter = 0
timer = 0
mapStruktur = copy.deepcopy(mapClean)
for i, pos in enumerate(possiblePos):
    start = getStartingPositionAndChar()
    if set(pos) == set((start[0], start[1])):
        continue
    mapStruktur[pos[0]][pos[1]] = "O"
    timer = time.time()
    if checkWay():
        # print(f"# DEBUG: Found possible Loop in {i+1}/{len(possiblePos)} placed trash @ {pos[0]}, {pos[1]}")
        counter += 1
    mapStruktur = copy.deepcopy(mapClean)

print (counter)
et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")
