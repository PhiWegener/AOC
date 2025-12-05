import time
st = time.process_time()
arr = []
with open("input/input.txt", "r") as inp:
    for line in inp:
        for number in line:
            arr.append(int(number))
# print(arr)
# 2333133121414131402
cnt = 0
result = []
for i, entry in enumerate(arr):
    if i%2 == 0:
        tmp = []
        for c in range(entry):
            tmp.append(cnt)
        result.append(tmp)
        cnt += 1
    else:
        tmp = []
        for c in range(entry):
            tmp.append(".")
        result.append(tmp)

# print(result)


for i in range(len(result)-1, 0, -1):
    insert = result[i]
    if "." in insert or len(insert) == 0:
        continue
    for j in range(len(result)-1):
        if j > i:
            break
        if not "." in result[j]:
            continue
        if len(insert) == len(result[j]):
            tmp = result[j]
            result[j] = insert
            result[i] = tmp
            break
        if len(insert) < len(result[j]):
            diff = len(result[j]) - len(insert)
            t = []
            for x in range(diff):
                t.append(".")
            tmp = []
            for x in range(len(result[j])-diff):
                tmp.append(".")
            result[j] = insert
            result.insert(j+1, t)
            result[i+1] = tmp
            break
    # if onlyNumbersToLeft(result, i):
    #     break
    # print(result)

# print(result)
final = []
for entry in result:
    for number in entry:
        if number == "." or len(entry) == 0: final.append(0)
        else: final.append(number)
    


checksum = 0
for i, entry in enumerate(final):
    checksum += entry * i
    # print(f"# DEBUG: adding to checksum: {entry} * {i} = {checksum}")

print(len(final))
print(checksum)
# gives 6.312.013.468.365 -> is wrong
et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")