import time, re
st = time.process_time()

patterns = []
designs = []

with open("input/input.txt", 'r') as file:
    for line in file:
        if "," in line:
            patterns = line.split(",")
            # print(patterns)
            continue
        if line == "\n":
            continue
        designs.append(line.strip())

patterns = sorted(patterns, key=len, reverse=True)
for i in range(len(patterns)):
    # print(entry)
    patterns[i] = patterns[i].strip().replace("\n", "")
    # if "g" in patterns[i] or len(patterns[i]) == 1:
    #     patterns.append(patterns[i])

search = "("
for i, pattern in enumerate(patterns):
    if i == len(patterns)-1:
        search += pattern + ")+"
        continue
    search += pattern + "|"

cnt = []
counter = 0
for i, design in enumerate(designs):
    debugOut = design + ": "
    # for pattern in patterns:    
    #     if pattern in design:
    #         design = design.replace(pattern, " ")
    #     else: 
    #         debugOut += pattern + "; "
    #         # print(pattern)
    design = re.sub(search, " ",design)    
    if design.strip() == "":
        counter += 1
    # else:
    #     print(design + "\n")
    

# 328 falsches Ergebnis  
# 287 falsches Ergebnis      
print(counter)
print(cnt)
et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")