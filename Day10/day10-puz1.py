import time
st = time.process_time()
tmp = []
matrix = []

# Testinput Ergebnisse: 9 Trailheads mit Score -> 5, 6, 5, 3, 1, 3, 5, 3, 5 ergibt 36
with open("input/input.txt", 'r') as file:
    for line in file:
        for number in line:
            if not number == "\n":
                tmp.append(int(number))
        matrix.append(tmp)
        tmp = []

def findTrails():
    # trailHead = (xcoord, ycoord)
    # print(f"# DEBUG: Start looking for trails with trailHead: {trailHead}")
    rows = len(matrix)
    cols = len(matrix[0])
    visitedEnpoints = set()
    startPoints = [] 

    def exploreTrail(xcoord, ycoord, numberCurPos):
        if not (0 <= xcoord < rows and 0 <= ycoord < cols):
            return False
        if matrix[xcoord][ycoord] != numberCurPos:
            return False
        if numberCurPos == 9:
            visitedEnpoints.add((xcoord, ycoord))
            return True
        directions = [
            (0, 1),  # rechts
            (0, -1), # links
            (1, 0),  # unten
            (-1, 0)  # oben
        ]
        temp = matrix[xcoord][ycoord]
        matrix[xcoord][ycoord] = "X"
        foundPath = False
        for dx, dy in directions:
            if exploreTrail(xcoord + dx, ycoord + dy, numberCurPos + 1):
                foundPath = True
        matrix[xcoord][ycoord] = temp
        return foundPath


    # counter = 0
    for xcoord, line in enumerate(matrix):
        for ycoord, number in enumerate(line):
            if number == 0:
                startPoints.append((xcoord, ycoord))

    pathCounts = {}
    for startPoint in startPoints:
        visitedEnpoints.clear()
        xcoord, ycoord = startPoint
        exploreTrail(xcoord, ycoord, 0)
        pathCounts[startPoint] = len(visitedEnpoints)
    
    return pathCounts


counter = 0
result = findTrails()
for startPoint, count in result.items():
    print(f"Startpunkt {startPoint}: {count} vollständige Pfade")
    counter += count
print(f"# ERGEBNIS: {counter}")

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")