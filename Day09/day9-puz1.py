import time
st = time.process_time()
arr = []
with open("input/input.txt", "r") as inp:
    for line in inp:
        for number in line:
            arr.append(int(number))
# print(arr)
cnt = 0
result = []
for i, entry in enumerate(arr):
    if i%2 == 0:
        for c in range(entry):
            result.append(cnt)
        cnt += 1        
    if i%2 != 0:
        for c in range(entry):
            result += "."       

# print(result)

def onlyNumbersToLeft(array, position):
    if position <= 0 or position >= len(array):
        return False
    return all(isinstance(array[i], int) for i in range(position))

for i in range(len(result)-1, 0, -1):
    insert = result[i]
    if insert == ".":
        continue
    for j in range(len(result)-1):
        if result[j] == ".":
            result[j] = insert
            break
    result[i] = "."
    if onlyNumbersToLeft(result, i):
        break
    # print(result)

# print(result)
checksum = 0
for i, entry in enumerate(result):
    if isinstance(entry, int):
        checksum += entry * i
        print(f"# DEBUG: adding to checksum: {entry} * {i} = {checksum}")


print(checksum)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")