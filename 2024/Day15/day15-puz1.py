import time
st = time.process_time()

matrix = []
movements = []
with open("input/input.txt", 'r') as file:
    for line in file:
        tmp = []
        if "#" in line:
            for char in line:
                if char == "\n":
                    continue
                tmp.append(char)
            matrix.append(tmp)
            continue
        if line == "\n":
            continue
        for char in line:
            if char == "\n":
                continue
            movements.append(char)

start = ()

for x, line in enumerate(matrix):
    if "@" in line:
        for y, char in enumerate(line):
            if char == "@":
                start = (x, y)
                break
        break

def checkNext(posToCheck, dx, dy):
    """returns the charakter of the next position"""
    cnt = 1
    if 0 <= posToCheck[0] < rows and 0 <= posToCheck[1] < cols:
        if matrix[posToCheck[0]][posToCheck[1]] == "#":
            return False, 0
        if matrix[posToCheck[0]][posToCheck[1]] == ".":
            return True, cnt
        if matrix[posToCheck[0]][posToCheck[1]] == "O":
            neighbor = (posToCheck[0] + dx, posToCheck[1] + dy)
            cnt += 1
            checkNext(neighbor)

directions = [(0,1), (1, 0), (0,-1), (-1,0)]
current = start
for direction in directions:
    dx, dy = direction
    neighbor = (current[0] + dx, current[1] + dy)
    if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols:
        if matrix[neighbor[0]][neighbor[1]] == "#":
            continue
        if matrix[neighbor[0]][neighbor[1]] == "O":
            noN = (neighbor[0] + dx, neighbor[1] + dy)
            if not checkNext(noN)[0]:
                continue
            


et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")