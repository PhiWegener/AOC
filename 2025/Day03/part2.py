import time
st = time.process_time()

devMode = False
devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

inputList = []
resultSum = 0

## BeispielInput ##
###################
# 987654321111111 #
# 811111111111119 #
# 234234234234278 #
# 818181911112111 #
###################
    
with open(inputFile, "r") as i:
    for line in i:
        inputList.append(line)

def getJoltList(inStr):
    return [int(char) for char in inStr.strip()]
    
for bank in inputList:
    jolts = getJoltList(bank)
    print(jolts)
    firstDigit = jolts[0]
    secondDigit = jolts[1]
    tmp = 0
    highestComb = 0
    for index, jolt in enumerate(jolts):
        if jolt > firstDigit and index < len(jolts)-1:
            firstDigit = jolt
            tmp = index
            secondDigit = jolts[index + 1]
        if jolt > secondDigit and index > tmp:
            secondDigit = jolt
    print(f"{firstDigit}{secondDigit}")
    highestComb = str(firstDigit) + str(secondDigit)
    resultSum += int(highestComb)
    continue

print(resultSum)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")