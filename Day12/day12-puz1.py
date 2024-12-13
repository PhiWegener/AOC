import time
st = time.process_time()
tmp = []
matrix = []

#   Y  0    1    2    3    4    5    6    7    8    9
# X   
# 0  ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F']
# 1  ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F']
# 2  ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F']
# 3  ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F']
# 4  ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E']
# 5  ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E']
# 6  ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E']
# 7  ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E']
# 8  ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E']
# 9  ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']

with open("input/input.txt", 'r') as file:
    for line in file:
        for flower in line:
            if not flower == "\n":
                tmp.append(flower)
        matrix.append(tmp)
        tmp = []


directions = {
    "up": {
        "dx": -1, 
        "dy": 0
    }, 
    "down": {
        "dx": 1,
        "dy": 0
    }, 
    "left": {
        "dx": 0,
        "dy": -1
    }, 
    "right": {
        "dx": 0,
        "dy": 1
    }
}


# direction oder: up -> down -> left -> right


listOfFlowerTypes = []
for line in matrix:
    for flower in line:
        if not flower in listOfFlowerTypes: listOfFlowerTypes.append(flower)

def findFields(plantType):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    startPoints = []
    area = 0
    bordercnt = 0
    
    def checkNeighbour(x, y, plantCurPos, plantType):
        # Anmerkung an mich: Schau dir Tag 10 an und orientier dich daran
        # Ich will von jedem R aus schauen, ob ich einen Weg aus dem aktuellen Pflanzentyp zum Startpunkt finde!
        # Wenn ja, dann füge ihn in Visited hinzu; Area +1; schau in alle Richtungen wegen Zaun (Zaun counter +1 pro nicht gleicher Buchstabe oder outOfIndex)
        # wenn Nein, dann neuer Startpunkt fürs nächste Feld und mit nächstem Buchstaben weiter
        # Logik bauen um die anderen startpunkte zu machen
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        if matrix[x][y] != plantCurPos:
            return False
        if plantCurPos == plantType:
            visited.add((x, y))

        for direction in directions: 
            nextPos = (currentPos[0]+direction["dx"], currentPos[1]+direction["dy"])
            if not 0 <= nextPos[0] < rowLen:
                bordercnt += 1
            if not 0 <= nextPos[1] < colLen:
                bordercnt += 1

    for xCoord, line in enumerate(matrix):
        for yCoord, plant in enumerate(line):
            currentPos = (xCoord, yCoord)
            if currentPos == plantType:
                area += 1
                checkNeighbours(currentPos)

for flower in listOfFlowerTypes:
    print(f"# DEBUG: Start with flowertype: {flower}")

result = findFields("I")


et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")