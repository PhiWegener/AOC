import time
st = time.process_time()
tmp = []
matrix = []

def createMatrix(x, y):
    """x und y sind die maximale Größe der Matrix"""
    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(".")
        matrix.append(tmp)


def getPath(prev, current):
    path = []
    while current is not None:
        path.append(current)
        current = prev[current]
    return path[::-1]

start = (0,0)
goal = (70,70)
createMatrix(goal[0]+1, goal[1]+1)

rows = len(matrix)
cols = len(matrix[0])
directions = [(0,1), (1, 0), (0,-1), (-1,0)]

with open("input/input.txt", 'r') as file:
    for row, line in enumerate(file):
        tmp = line.split(",")
        x, y = int(tmp[0]), int(tmp[1])
        matrix[y][x] = "#"
        if row <= 1024:
            continue
        queue = [start]
        visited = set()
        visited.add((start[0], start[1]))
        final = []
        path = {}
        path[start] = None

        while queue:
            current = queue.pop(0)
            if current == goal:
                final = getPath(path, goal)
            
            for dx, dy in directions:
                neighbour = (current[0] + dx, current[1] + dy)
                if (0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols and 
                        matrix[neighbour[0]][neighbour[1]] == "." and
                        neighbour not in visited):
                    queue.append(neighbour)
                    visited.add(neighbour)
                    path[neighbour] = current
        if len(final) == 0:
            print(line)
            break

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")