import time
st = time.process_time()

part1Toggle = True
por = []
updates = []
dictPor = {}
# Lösung wäre 5900 (laut Berni)
with open("input/input.txt", "r") as i:
    for line in i:
        if line == "\n":
            part1Toggle = False
            continue
        if part1Toggle:
            key, value = map(int, line.split("|"))
            if key not in dictPor:
                dictPor[key] = []
            dictPor[key].append(value)
            continue
        updates.append(list(map(int, line.split(","))))
        
# print(dictPor)
# print(updates)
falseUpdates = []
def checkOrder(currUpdateIndex, update):
    page = update[currUpdateIndex]
    # rules = [r for r in por if r[0] == page]
    for rule in dictPor.keys():
        if rule == update[currUpdateIndex]:
            for number in dictPor[rule]:
                for i in range(0, currUpdateIndex):
                    if update[i] == number:
                        return False
    return True

def sort(update):
    def violatesRules(sortedPart, value):
        for v in sortedPart:
            if not value in dictPor.keys(): continue
            if v == dictPor[value]:
                return True
        return False
    for i in range(1, len(update)):
        key = update[i]
        j = i-1

        while j >= 0 and violatesRules(update[j:j+1], key):
            update[j+1] = update[j]
            j -= 1
        update[j+1] = key
    return update

resultList = []
# toggle = True
for updateNumber, update in enumerate(updates):
    # print(f"###\n# DEBUG: Start for line {updateNumber}")
    for currUpdateIndex, page in enumerate(update):
        # ret = sort(currUpdateIndex, update)
        if not checkOrder(currUpdateIndex, update):
            falseUpdates.append(update)
            # resultList.append(ret[1][int(len(update)/2-0.5)])
            break
    
# print(f"# DEBUG: falseUpdates {falseUpdates}")
test = []
for update in falseUpdates:
    print(f"# DEBUG: update before sort {update}")
    test = sort(update)
    print(f"# DEBUG: update after sort {test}")

# 51346 => too High
# len -> 862 Falsche ?
print(len(falseUpdates))
# print(sum(resultList))

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")