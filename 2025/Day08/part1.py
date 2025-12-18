import time
import heapq
from itertools import combinations
st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
    limit = 10
else:
    inputFile = "input.txt"
    limit = 1000

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

def union(a, b, parent, size):
    ra = find(a, parent)
    rb = find(b, parent)

    if ra == rb:
        return
    
    parent[rb] = ra
    size[ra] += size[rb]

heap: list[(int, int, int)] = []
n = len(inputList)

for a, b in combinations(range(n), 2):
    distance = calcDistance(inputList[a], inputList[b])
    item = (-distance, a, b)
    
    if len(heap) < limit:
        heapq.heappush(heap, item)
    else:
        if item > heap[0]:
            heapq.heapreplace(heap, item)
    heap.sort(key=getFirstElement)

parent = list(x for x in range(len(inputList)))
size = list(1 for x in range(len(inputList)))

for negDist, a, b in reversed(heap):
    union(a, b, parent, size)

componentSizes = {}
for v in range(n):
    r = find(v, parent)
    componentSizes[r] = size[r]

top3 = sorted(componentSizes.values(), reverse=True)[:3]
result = top3[0]*top3[1]*top3[2]

print(result)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")