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
resultSum = 0


    
with open(inputFile, "r") as i:
    for line in i:
        inputList = line.split(",")

for idRange in inputList:
    # print(f"FakeId: {idRange}")
    startRange, endRange = idRange.split("-") 
    for entry in list(range(int(startRange), int(endRange)+1)):
        strEntry = str(entry)
        if re.fullmatch(r"(.+)\1+", strEntry):
            # print(f"Gefundene FakeID: {strEntry}")
            resultSum = resultSum + entry


print(resultSum)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")