import time
from itertools import combinations
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

def calcArea(p1, p2):
    # Flächenberechnung eines Rechtecks mit 2 Punkten(gegenüberliegende Ecken)
    # Kantenlängen:
    dx = abs(p2[0] - p1[0]) + 1
    dy = abs(p2[1] - p1[1]) + 1
    return(dx*dy)

maxResult = 0
n = len(inputList)

for a, b in combinations(range(n), 2):
    area = calcArea(inputList[a], inputList[b])
    # print(a, b, "=", area)
    if area < maxResult:
        continue
    
    maxResult = area

print(maxResult)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")