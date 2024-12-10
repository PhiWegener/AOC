import time
st = time.process_time()

tmp = []
mapStruktur = []
with open("input/input.txt", 'r') as file:
    for line in file:
        for letter in line:
            if not letter == "\n":
                tmp.append(letter)
        mapStruktur.append(tmp)
        tmp = []
# print(mapStruktur)    

directions = {
    "diagLeftUp": {
        "dx": -1,
        "dy": -1
    },
    "diagRightUp": {
        "dx": -1,
        "dy": 1
    },
    "diagRightDown": {
        "dx": 1,
        "dy": 1
    },
    "diagLeftDown": {
        "dx": 1,
        "dy": -1
    }
}
counter = 0
for xCord, line in enumerate(mapStruktur):
    for yCord, letter in enumerate(line):
        if letter == "A":
            if xCord-1 < 0 or xCord+1 >= len(mapStruktur)-1:
                continue
            if yCord-1 < 0 or yCord+1 >= len(line)-1:
                continue
            
            print(f"# DEBUG: Found Character A start checking for X-MAS ({xCord}, {yCord})")

            # 2 Cases Möglich: S oder M links über A
            # Case 1 (M ist links oben):
            direction = directions["diagLeftUp"]
            if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                direction = directions["diagRightDown"]
                if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                    continue
                direction = directions["diagRightUp"]
                if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                        continue
                elif mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                        continue
                else:
                    continue    
                print(f"# DEBUG: Case 1 Korrekt Counter {counter} + 1")
                counter += 1
                    
            # Case 2 (S ist links oben):
            elif mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                direction = directions["diagRightDown"]
                if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                    continue
                direction = directions["diagRightUp"]
                if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                        continue
                elif mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                        continue
                else:
                    continue
                print(f"# DEBUG: Case 2 Korrekt Counter {counter} + 1")
                counter += 1

print(counter)

et = time.process_time()
print(f"\nZeit: {(et-st)*1000}ms")