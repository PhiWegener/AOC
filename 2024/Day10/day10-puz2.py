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
    completeTrailCounts = {}

    def exploreTrail(xcoord, ycoord, numberCurPos):
        if not (0 <= xcoord < rows and 0 <= ycoord < cols):
            return 0
        if matrix[xcoord][ycoord] != numberCurPos:
            return 0
        if numberCurPos == 9:
            return 1
        directions = [
            (0, 1),  # rechts
            (0, -1), # links
            (1, 0),  # unten
            (-1, 0)  # oben
        ]
        totalTrails = 0
        for dx, dy in directions:
            totalTrails += exploreTrail(xcoord + dx, ycoord + dy, numberCurPos + 1)

        return totalTrails


    # counter = 0
    for xcoord, line in enumerate(matrix):
        for ycoord, number in enumerate(line):
            if number == 0:
                if (xcoord, ycoord) not in completeTrailCounts.keys():
                    completeTrailCounts[(xcoord, ycoord)] = 0
                completeTrailCounts[(xcoord, ycoord)] += exploreTrail(xcoord, ycoord, 0)
    return completeTrailCounts


counter = 0
result = findTrails()
for startPoint, count in result.items():
    print(f"Startpunkt {startPoint}: {count} vollständige Pfade")
    counter += count
print(f"# ERGEBNIS: {counter}")

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")