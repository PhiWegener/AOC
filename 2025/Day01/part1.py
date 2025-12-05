import time
st = time.process_time()

devMode = False

# 333 too low

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

inputList = []
currentPosition = 50
counter = 0

with open(inputFile, "r") as i:
    for line in i:
        inputList.append(line)

for entry in inputList:
    if entry.startswith("L"):
        currentPosition = currentPosition - int(entry.split("L")[1])
        # print(f"not processed: {currentPosition}" )
        while currentPosition < 0:
            currentPosition = 100 - abs(currentPosition)
        print(currentPosition)
    if entry.startswith("R"):
        currentPosition = currentPosition + int(entry.split("R")[1])
        while currentPosition > 99:
            currentPosition = currentPosition - 100
        print(currentPosition)

    if currentPosition == 0:
        counter += 1

print(counter)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")