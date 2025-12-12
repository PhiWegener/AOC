import time
st = time.process_time()

devMode = False
# devMode = True

if devMode:
    inputFile = "example.txt"
else:
    inputFile = "input.txt"

ranges = []
result = 0

with open(inputFile, "r") as i:
    for line in i:
        if line == "\n":
            continue
        if "-" in line:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
            continue            

ranges = sorted(ranges)
merged = [ranges[0]]

for start, end in ranges[1:]:
    lastStart, lastEnd = merged[-1]
    if start <= lastEnd:
        merged[-1] = (lastStart, max(lastEnd, end))
    else:
        merged.append((start, end))

for start, end in merged:
    result += end - start + 1

print(result)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")