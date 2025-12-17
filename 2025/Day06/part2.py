import time
import re
st = time.process_time()

devMode = False
devMode = True

if devMode:
    inputFile = "example.txt"
    length = 4
else:
    inputFile = "input.txt"
    length = 5

result = 0

mathProblems = []

with open(inputFile, "r") as i:
    for index, line in enumerate(i):
        # print(line)
        line = line.rstrip("\n")
        j = 0
        while j < len(line):
            chunk = line[j:j+length-1]
            if index == 0:
                mathProblems.append([chunk])
                j += length
                continue
            mathProblems[j//length].append(chunk)
            j += length


for mathProblem in mathProblems:
    for x, row in enumerate(mathProblem):
        if x > 0:
            break
        math = mathProblem[-1].strip()
        tmp = []
        i = 0
        while i < len(mathProblem)-1:
            j = 0
            tmpVar = ""
            while j < len(mathProblem[i]):
                if mathProblem[x+j][i] == " ":
                    j += 1
                    continue
                tmpVar = tmpVar + mathProblem[x+j][i]
                j += 1
                continue
            if tmpVar != "":
                tmp.append(tmpVar)
            i += 1
            continue

        
        if math == "*":
            intRes = 1
            for e in tmp:
                intRes = intRes * int(e)
        if math == "+":
            intRes = 0
            for e in tmp:
                intRes = intRes + int(e)
        # print(intRes)
        result += intRes

# too high: 14238091348462
print(result)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")