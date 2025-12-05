import time
import re
st = time.process_time()

# Example Input Data Parse
# {
#     "priceA": 3,
#     "priceB": 1,
#     "machines": [
#         {
#             "buttonA": {
#                 "x": 94,
#                 "y": 34
#             },
#             "buttonB": {
#                 "x": 22,
#                 "y": 67
#             },
#             "prize": {
#                 "x": 8400,
#                 "y": 5400
#             }
#         },
#         {
#             "buttonA": {
#                 "x": 26,
#                 "y": 66
#             },
#             "buttonB": {
#                 "x": 67,
#                 "y": 21
#             },
#             "prize": {
#                 "x": 12748,
#                 "y": 12176
#             }
#         },
#         {
#             "buttonA": {
#                 "x": 17,
#                 "y": 86
#             },
#             "buttonB": {
#                 "x": 84,
#                 "y": 37
#             },
#             "prize": {
#                 "x": 7870,
#                 "y": 6450
#             }
#         },
#         {
#             "buttonA": {
#                 "x": 69,
#                 "y": 23
#             },
#             "buttonB": {
#                 "x": 27,
#                 "y": 71
#             },
#             "prize": {
#                 "x": 18641,
#                 "y": 10279
#             }
#         }
#     ]
# }

clawMachine = {
    "priceA": 3,
    "priceB": 1,
    "machines": [{}]
}

with open("input/input.txt", "r") as i:
    machineIndex = 0
    for line in i:
        if line == "\n":
            machineIndex += 1
            clawMachine["machines"].append({})
            continue
        if "Button A" in line:
            if not "buttonA" in clawMachine["machines"][machineIndex].keys():
                clawMachine["machines"][machineIndex]["buttonA"] = {
                    "x": int(re.findall(r"X\+[0-9]+",line)[0].split("+")[1]), 
                    "y": int(re.findall(r"Y\+[0-9]+", line)[0].split("+")[1])}
        if "Button B" in line:
            if not "buttonB" in clawMachine["machines"][machineIndex].keys():
                clawMachine["machines"][machineIndex]["buttonB"] = {
                    "x": int(re.findall(r"X\+[0-9]+",line)[0].split("+")[1]), 
                    "y": int(re.findall(r"Y\+[0-9]+", line)[0].split("+")[1])}
        if "Prize" in line:
            if not "prize" in clawMachine["machines"][machineIndex].keys():
                clawMachine["machines"][machineIndex]["prize"] = {
                    "x": int(re.findall(r"X=[0-9]+",line)[0].split("=")[1]), 
                    "y": int(re.findall(r"Y=[0-9]+", line)[0].split("=")[1])}

# Using Cramer's Rule to solve the Problem the mathematical way
counter = 0
for cm in clawMachine["machines"]:
    butA = cm["buttonA"]
    butB = cm["buttonB"]
    prizeX = cm["prize"]["x"]
    prizeY = cm["prize"]["y"]

    #berechne determinante
    det = butA["y"]*butB["x"]-butA["x"]*butB["y"]

    a = (prizeY*butB["x"]-prizeX*butB["y"])/det
    b = (prizeX*butA["y"]-prizeY*butA["x"])/det
    # print(a, b)
    if a.is_integer() and b.is_integer():
        counter += a*clawMachine["priceA"] + b*clawMachine["priceB"]

print(int(counter))
et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")