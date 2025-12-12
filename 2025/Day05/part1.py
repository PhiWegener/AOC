import time
st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

idsToCheck = []
freshIdRange = []
counter = 0

with open(inputFile, "r") as i:
    for line in i:
        if line == "\n":
            continue
        if "-" in line:
            start, end = line.split("-")
            freshIdRange.append((start, end))
            continue
        idsToCheck.append(int(line.strip()))


for i in idsToCheck:
    switch = False
    for r in freshIdRange:
        if switch:
            continue

        if int(r[0]) <= i <= int(r[1]):
            counter += 1
            switch = True

        
# 824 too high

print(counter)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")