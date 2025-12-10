import time
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
    startRange, endRange = idRange.split("-") 
    for entry in list(range(int(startRange), int(endRange)+1)):
        strEntry = str(entry)
        if len(strEntry)%2 != 0:
            continue
        firstHalf, secondHalf = strEntry[:len(strEntry)//2], strEntry[len(strEntry)//2:]
        # print(firstHalf, secondHalf)
        if firstHalf == secondHalf:
            resultSum = resultSum + entry


print(resultSum)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")