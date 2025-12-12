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
        inputList.append(line)

def getJoltList(inStr):
    return [int(char) for char in inStr.strip()]

def getHighestJoltWithEnoughSpace(bank, neededSpace, startIndex):
    pos = startIndex + 1
    currentHighest = bank[startIndex+1]
    for index in range(startIndex + 1, len(bank)):
        jolt = bank[index]
        if jolt > currentHighest and len(bank) - index >= neededSpace and index > startIndex:
            currentHighest = jolt
            pos = index
    return currentHighest, pos
    
for bank in inputList:
    jolts = getJoltList(bank)
    firstDigit, firstIndex = getHighestJoltWithEnoughSpace(jolts, 12, -1)
    secondDigit, secondIndex = getHighestJoltWithEnoughSpace(jolts, 11, firstIndex)
    thirdDigit, thirdIndex = getHighestJoltWithEnoughSpace(jolts, 10, secondIndex)
    fourthDigit, fourthIndex = getHighestJoltWithEnoughSpace(jolts, 9, thirdIndex)
    fifthDigit, fifthIndex = getHighestJoltWithEnoughSpace(jolts, 8, fourthIndex)
    sixthDigit, sixthIndex = getHighestJoltWithEnoughSpace(jolts, 7, fifthIndex)
    seventhDigit, seventhIndex = getHighestJoltWithEnoughSpace(jolts, 6, sixthIndex)
    eighthDigit, eighthIndex = getHighestJoltWithEnoughSpace(jolts, 5, seventhIndex)
    ninthDigit, ninthIndex = getHighestJoltWithEnoughSpace(jolts, 4, eighthIndex)
    tenthDigit, tenthIndex = getHighestJoltWithEnoughSpace(jolts, 3, ninthIndex)
    eleventhDigit, eleventhIndex = getHighestJoltWithEnoughSpace(jolts, 2, tenthIndex)
    twelfthDigit, twelfthIndex = getHighestJoltWithEnoughSpace(jolts, 1, eleventhIndex)

    highestComb = f"{firstDigit}{secondDigit}{thirdDigit}{fourthDigit}{fifthDigit}{sixthDigit}{seventhDigit}{eighthDigit}{ninthDigit}{tenthDigit}{eleventhDigit}{twelfthDigit}"
    resultSum += int(highestComb)
    continue

print(resultSum)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")