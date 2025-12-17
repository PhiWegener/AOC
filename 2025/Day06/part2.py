import time
import re
st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

result = 0

mathProblems = []
chunkSizes = []

with open(inputFile, "r") as i:
    content = i.read()
    lastLine = content.splitlines()[-1] + " "
    # lastLine = "*   +   *   +  "
    for chunk in re.findall(r"[*+]?\s+", lastLine.rstrip("\n")):
        chunkSizes.append(len(chunk))
    
    for index, line in enumerate(content.splitlines()):
        # print(line)
        line = line.rstrip("\n")
        j = 0
        n = 0
        if index == 0:
            length = chunkSizes[0]
        while j < len(line):
            length = chunkSizes[n]
            chunk = line[j:j+length-1]
            if index == 0:
                mathProblems.append([chunk])
                j += length
                n += 1
                continue 
            mathProblems[n].append(chunk)
            n += 1
            j += length

for mathProblem in mathProblems:
    for x, row in enumerate(mathProblem):
        if x > 0:
            break
        math = mathProblem[-1].strip()
        tmp = []
        i = 0
        while i < len(mathProblem[0]):
            j = 0
            tmpVar = ""
            while j < len(mathProblem)-1:
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
        result += intRes

# too high: 14238091348462
print(result)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")