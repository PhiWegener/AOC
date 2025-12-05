import time
st = time.process_time()

# doesn't work

countSafe = 0
listOfUnsafes = []
def checkIfIntListIsSafe(intList):
    inc = False
    dec = False
    tmpList = []
    for i in range(len(intList) - 1):
        if i == 0:
            if intList[0]<intList[-1]:
                inc = True
            else:
                dec = True

        diff = intList[i] - intList[i+1]

        if diff == 0:
            if not len(tmpList) >= 1:
                tmpList.append(intList[i])
            else:
                return False
        if inc:
            if diff > 0 or diff < -3:
                if not len(tmpList) >= 1:
                    tmpList.append(intList[i])
                else:
                    return False
        if dec:
            if diff < 0 or diff > 3:
                if not len(tmpList) >= 1:
                    tmpList.append(intList[i])
                else:
                    return False
        print(tmpList)
    
    return True

with open("input/input.txt", "r") as i:
    for line in i:
        # print("############### next line #############")
        # print(line)
        intList = list(map(int, line.split()))
        if checkIfIntListIsSafe(intList):
            countSafe += 1
        else:
            listOfUnsafes.append(intList)

print(countSafe)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")