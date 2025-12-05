import time
import re
st = time.process_time()

patterns = []
designs = []

with open("input/input.txt", 'r') as file:
    for line in file:
        if "," in line:
            patterns = line.split(",")
            continue
        if line == "\n":
            continue
        designs.append(line.strip())

patterns = sorted(patterns, key=len, reverse=True)
for i in range(len(patterns)):
    patterns[i] = patterns[i].strip().replace("\n", "")
    # if "g" in patterns[i] or len(patterns[i]) == 1:
    #     patterns.append(patterns[i])

search = r"("
for i, pattern in enumerate(patterns):
    if i == len(patterns)-1:
        search += pattern + ")+"
        continue
    search += pattern + "|"

# search = re.compile(search)
counter = 0
for design in designs:
    print(f"search: {search}")
    if re.fullmatch(search, design):
        counter += 1   

# 328 falsches Ergebnis  
# 287 falsches Ergebnis      
print(counter)
et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")