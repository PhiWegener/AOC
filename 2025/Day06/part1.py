import time
import re
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
        # print(line)
        inputList.append(re.split(r"\s+", line.strip()))

for y, row in enumerate(inputList):
    if y > 0:
        break
    for x, col in enumerate(row):
        if x == len(row):
            continue
        math = inputList[-1][x]
        i = 1
        intRes = int(col)
        while i < len(inputList)-1:
            if math == "*":
                intRes = intRes * int(inputList[y+i][x])
                i += 1
            if math == "+":
                intRes = intRes + int(inputList[y+i][x])
                i += 1
        print(intRes)
        result += intRes
    
print(result)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")