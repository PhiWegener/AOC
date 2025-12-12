import time
st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

inputList = []
result = 0

with open(inputFile, "r") as i:
    for line in i:
        inputList.append(line.strip())

def removeRolls(removable):
    for x, y in removable:
        row = list(inputList[y])
        row[x] = "x"
        inputList[y] = "".join(row)
    return inputList


while True:
    counter = 0
    removable = []
    for y, line in enumerate(inputList):
        for x, letter in enumerate(line):
            amntRolls = 0
            if  letter == "." or letter == "x":
                continue
            # links oben
            if y-1 >= 0 and x-1 >= 0 and inputList[y-1][x-1] == "@":
                amntRolls += 1
            # oben
            if y-1 >= 0 and inputList[y-1][x] == "@":
                amntRolls += 1
            # rechts oben
            if y-1 >= 0 and x+1 < len(line) and inputList[y-1][x+1] == "@":
                amntRolls += 1
            # rechts
            if x+1 < len(line) and inputList[y][x+1] == "@":
                amntRolls += 1
            # rechts unten
            if y+1 < len(inputList) and x+1 < len(line) and inputList[y+1][x+1] == "@":
                amntRolls += 1
            # unten
            if y+1 < len(inputList) and inputList[y+1][x] == "@":
                amntRolls += 1
            # links unten
            if y+1 < len(inputList) and x-1 >= 0 and inputList[y+1][x-1] == "@":
                amntRolls += 1
            # links
            if x-1 >= 0 and inputList[y][x-1] == "@":
                amntRolls += 1

            if amntRolls < 4:
                counter += 1
                result += 1
                removable.append((x, y))
    
    inputList = removeRolls(removable)
            
    if counter == 0:
        break

            

print(result)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")