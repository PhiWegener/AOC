import time
import heapq
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

def getFirstElement(tuple):
    return tuple[0]

def calcDistance(p1, p2):
    # entfernung=wurzel[ (x2-x1)²+(y2-y1)²+(z2-z1)² ]
    # wurzel kann weggelassen werden (ist ja relativ)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return(dx*dx + dy*dy + dz*dz)

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    ra = find(a, parent)
    rb = find(b, parent)

    if ra == rb:
        return False
    
    parent[rb] = ra
    return True

heap: list[(int, int, int)] = []
n = len(inputList)

for a, b in combinations(range(n), 2):
    distance = calcDistance(inputList[a], inputList[b])
    item = (-distance, a, b)
    heapq.heappush(heap, item)
    
heap.sort(key=getFirstElement)

parent = list(x for x in range(len(inputList)))
components = n
lastEdge = None
for negDist, a, b in reversed(heap):
    if union(a, b, parent):
        components -= 1
        lastEdge = (a, b)
        if components == 1:
            break

# print(parent)
print(inputList[lastEdge[0]][0] * inputList[lastEdge[1]][0])

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")