countSafe = 0
def checkIfIntListIsSafe(intList):
    inc = False
    dec = False
    for i in range(len(intList) - 1):
        if i == 0:
            if intList[0]<intList[-1]:
                inc = True
            else:
                dec = True

        diff = intList[i] - intList[i+1]

        if diff == 0:
            return False
        if inc:
            if diff > 0 or diff < -3:
                return False
        if dec:
            if diff < 0 or diff > 3:
                return False

    return True

with open("input/input.txt", "r") as i:
    for line in i:
        # print("############### next line #############")
        # print(line)
        intList = list(map(int, line.split()))
        if checkIfIntListIsSafe(intList):
            countSafe += 1
    
print(countSafe)