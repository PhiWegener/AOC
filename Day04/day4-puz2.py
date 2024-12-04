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
    # print(f"# DEBUG: Start searching for \'X\' in Line {xCord} ({line})")
    for yCord, letter in enumerate(line):
        # print(f"# DEBUG: Start searching for X at Position {yCord}")
        if letter == "A":
            if xCord < 2 :
                continue
            if xCord > len(mapStruktur) -3:
                continue
            if yCord > len(line) -3:
                continue
            if yCord < 2:
                continue

            print(f"# DEBUG: Found Character A start checking for X-MAS @({xCord}, {yCord})")

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
                direction = directions["diagRightUp"]
                if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                        continue
                    print(f"# DEBUG: Case 1 Korrekt Counter +1")
                    counter += 1
                    
            # Case 2 (S ist links oben):
            direction = directions["diagLeftUp"]
            if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                direction = directions["diagRightDown"]
                if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                    continue
                direction = directions["diagRightUp"]
                if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                        continue
                direction = directions["diagRightUp"]
                if mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "M":
                    direction = directions["diagLeftDown"]
                    if not mapStruktur[xCord + direction["dx"]][yCord + direction["dy"]] == "S":
                        continue
                    print(f"# DEBUG: Case 2 Korrekt Counter +1")
                    counter += 1

print(counter)
