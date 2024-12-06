import time
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


def getStartingPositionAndChar():
    # get starting position
    for xCoord in range(len(mapStruktur) -1):
        for yCoord, char in enumerate(mapStruktur[xCoord]):
            if char == "." or char == "#":
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
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#":
            nextPosition = [currentPosition[0], currentPosition[1]+1]
            mapStruktur[nextPosition[0]][nextPosition[1]] = ">"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = "^"
        return nextPosition, mapStruktur[nextPosition[0]][nextPosition[1]]
    except IndexError:
        return currentPosition, mapStruktur[nextPosition[0]][nextPosition[1]]
        
def moveRight(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X"
    try:
        nextPosition = [currentPosition[0], currentPosition[1]+1]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#":
            nextPosition = [currentPosition[0]+1, currentPosition[1]]
            mapStruktur[nextPosition[0]][nextPosition[1]] = "v"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = ">"
        return nextPosition, mapStruktur[nextPosition[0]][nextPosition[1]]
    except IndexError:
        return currentPosition, mapStruktur[nextPosition[0]][nextPosition[1]]

def moveDown(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X"
    try:
        nextPosition = [currentPosition[0]+1, currentPosition[1]]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#":
            nextPosition = [currentPosition[0], currentPosition[1]-1]
            mapStruktur[nextPosition[0]][nextPosition[1]] = "<"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = "v"
        return nextPosition, mapStruktur[nextPosition[0]][nextPosition[1]]
    except IndexError:
        return currentPosition, mapStruktur[nextPosition[0]][nextPosition[1]]

def moveLeft(currentPosition):
    mapStruktur[currentPosition[0]][currentPosition[1]] = "X"
    try:
        nextPosition = [currentPosition[0], currentPosition[1]-1]
        if mapStruktur[nextPosition[0]][nextPosition[1]] == "#":
            nextPosition = [currentPosition[0]-1, currentPosition[1]]
            mapStruktur[nextPosition[0]][nextPosition[1]] = "^"
        else: 
            mapStruktur[nextPosition[0]][nextPosition[1]] = "<"
        return nextPosition, mapStruktur[nextPosition[0]][nextPosition[1]]
    except IndexError:
        return currentPosition, mapStruktur[nextPosition[0]][nextPosition[1]]


xCoordStart, yCoordStart, char = getStartingPositionAndChar()
currentPosition = [xCoordStart, yCoordStart]
while True:
    if char == "^":
        currentPosition = moveUp(currentPosition)
        char = mapStruktur[currentPosition[0]][currentPosition[1]]
    if char == ">":
        currentPosition = moveRight(currentPosition)
        char = mapStruktur[currentPosition[0]][currentPosition[1]]
    if char == "v":
        currentPosition = moveDown(currentPosition)
        char = mapStruktur[currentPosition[0]][currentPosition[1]]
    if char == "<":
        currentPosition = moveLeft(currentPosition)
        char = mapStruktur[currentPosition[0]][currentPosition[1]]
    if char == "X":
        break

counter = 0
for line in mapStruktur:
    # print(line)
    counter += line.count("X")
print (counter)

et = time.process_time()
print(f"Zeit: {(et-st)*1000}ms")