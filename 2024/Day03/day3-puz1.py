import time
st = time.process_time()

import re
searchRegex = "mul\(\d{1,3},\d{1,3}\)"
listOfMultiplies = []
with open("input/input.txt", "r") as i:
    for line in i:
        listOfMultiplies.append(re.findall(searchRegex, line))
print(listOfMultiplies)
    
def mul(x,y):
    return x * y

resultMult = []
for listTmp in listOfMultiplies:
    for entry in listTmp:
        exec(f"x={entry}")
        resultMult.append(x)

print(sum(resultMult))

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")