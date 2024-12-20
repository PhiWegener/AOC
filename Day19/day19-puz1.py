import time
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


for i in range(len(patterns)):
    # print(entry)
    patterns[i] = patterns[i].strip().replace("\n", "")

patterns = sorted(patterns, key=len, reverse=True)
counter = 0
for design in designs:
    for pattern in patterns:    
        if pattern in design:
            design = design.replace(pattern, "")
    if design == "":
        counter += 1

# 328 falsches Ergebnis        
print(counter)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")