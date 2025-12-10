import time
st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

# 6513 too high
# 5274 too low
# 5403 too low
# 6496 correct

inputList = []
currentPosition = 50
counter = 0

with open(inputFile, "r") as i:
    for line in i:
        inputList.append(line)

for entry in inputList:
    if entry.startswith("L"):
        amtRotations = int(entry.split("L")[1])
        while amtRotations != 0:
            currentPosition -= 1
            amtRotations -= 1
            if currentPosition < 0:
                currentPosition = 99
            if currentPosition == 0 and amtRotations > 0:
                counter += 1

    if entry.startswith("R"):
        amtRotations = int(entry.split("R")[1])
        while amtRotations != 0:
            currentPosition += 1
            amtRotations -= 1
            if currentPosition >= 100:
                currentPosition = 0
            if currentPosition == 0 and amtRotations > 0:
                counter += 1

    if currentPosition == 0:
        counter += 1

print(counter)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")