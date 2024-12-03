import re
searchRegex = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
listOfMultiplies = []
inputStr = ""
with open("input/input.txt", "r") as i:
    for line in i:
        inputStr += line.replace("\r\n", "")

listOfMultiplies = re.findall(searchRegex, inputStr)
# print(listOfMultiplies)
    
def mul(x,y):
    return x * y
toggle = True
listTmp = []
for i in listOfMultiplies:
    if i == "don't()":
        toggle = False
        continue
    if i == "do()":
        toggle = True
        continue
    
    if toggle:
        exec(f"x={i}")
        listTmp.append(x)
    else:
        continue
print(sum(listTmp))