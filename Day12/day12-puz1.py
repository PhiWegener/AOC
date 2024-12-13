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

def checkborder(xCoord, yCoord):
    """
    returns True if xCoord and yCoord are both inside Mapborders
    """
    if not (0 <= xCoord < len(matrix)):
        return False
    if not (0 <= yCoord < len(matrix[0])):
        return False
    return True

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


def checkEndOfField(flowerType, xCoord, yCoord):
    """Returns True if the current Field is the end of the flowerfield!"""
    cnt = 0
    for key, direction in directions.items():
        match key:
            case "up":
                if xCoord + direction["dx"] < 0:
                    cnt += 1
                elif matrix[xCoord + direction["dx"]][yCoord + direction["dy"]] != flowerType:
                    cnt += 1
            case "down":
                if xCoord + direction["dx"] >= len(matrix):
                    cnt += 1
                elif matrix[xCoord + direction["dx"]][yCoord + direction["dy"]] != flowerType:
                    cnt += 1
            case "left":
                if yCoord + direction["dy"] < 0:
                    cnt += 1
                elif matrix[xCoord + direction["dx"]][yCoord + direction["dy"]] != flowerType:
                    cnt += 1
            case "right":
                if yCoord + direction["dy"] >= len(matrix[0]):
                    cnt += 1
                elif matrix[xCoord + direction["dx"]][yCoord + direction["dy"]] != flowerType:
                    cnt += 1
        if cnt >= 3:
            return True
        return False

# direction oder: up -> down -> left -> right
def findField(flowerType):
    borderCnt = 0
    area = 0
    price = 0
    for xCoord, line in enumerate(matrix):
        for yCoord, flower in enumerate(line):
            current = (xCoord, yCoord)
            if matrix[current[0]][current[1]] != flowerType:
                continue
            for direction in directions.values():
                if not checkborder(current[0] + direction["dx"], current[1] + direction["dy"]): 
                    borderCnt += 1
                    continue
                if matrix[current[0]+direction["dx"]][current[1]+direction["dy"]] != flowerType:
                    borderCnt += 1
            area += 1
            if checkEndOfField(flowerType, xCoord, yCoord):
                price += borderCnt * area
                print(f"# DEBUG: End of Field {flowerType}: ({borderCnt}, {area}) = {price}")
    return price



listOfFlowerTypes = []
for line in matrix:
    for flower in line:
        if not flower in listOfFlowerTypes: listOfFlowerTypes.append(flower)

cnt = 0
for flower in listOfFlowerTypes:
    print(f"# DEBUG: Start with flowertype: {flower}")
    cnt += findField(flower)
print(cnt)


et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")