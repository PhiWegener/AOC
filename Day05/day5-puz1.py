part1Toggle = True
por = []
updates = []
with open("input/input.txt", "r") as i:
    for line in i:
        if line == "\n":
            part1Toggle = False
            continue
        if part1Toggle:
            tmp = tuple(map(int, line.split("|")))
            por.append(tmp)
            continue
        updates.append(list(map(int, line.split(","))))
        
# print(por)
# print(updates)

def checkOrder(page, index, update):
    rules = [r for r in por if r[0] == page]
    if index == 0:
        return True
    for rule in rules:
        for i in range(0, index):
            if update[i] == rule[1]:
                print(f"# DEBUG: rule wurde nicht erfüllt: {rule}, in line{update}")
                return False
    return True
    
counter = 0
resultList = []
# toggle = True
for updateNumber, update in enumerate(updates):
    toggle = True
    for index, page in enumerate(update):
        # print(checkOrder(page, index, por, update))
        if not checkOrder(page, index, update):
            toggle = False
            counter += 1
    if toggle:
        print(f"# DEBUG: Found correct entry in line {updateNumber}")
        resultList.append(update[int(len(update)/2-0.5)])



# counter -> 1241 Falsche
print(counter)
print(sum(resultList))