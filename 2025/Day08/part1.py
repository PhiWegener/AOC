import time
st = time.process_time()

devMode = False
devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

inputList = []

with open(inputFile, "r") as i:
    for line in i:
        inputList.append(line.rstrip("\n"))











print(len(positionOfSplitters))

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")