tmp = []
mapStruktur = []

# Aufbau Map wobei X die senkrechte Koordinate ist und Y die Waagerechte
# 
#     ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], 
#     ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], 
#     ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], 
#     ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], 
#     ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], 
#     ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], 
#     ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], 
#     ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], 
#     ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], 
#     ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
# 

with open("input/input.txt", 'r') as file:
    for line in file:
        for letter in line:
            if not letter == "\n":
                tmp.append(letter)
        mapStruktur.append(tmp)
        tmp = []
# print(mapStruktur)    

directions = {
    "up": {
        "dx": -1,
        "dy": 0
    },
    "down": {
        "dx": 1,
        "dy": 0
    },
    "left": {
        "dx": 0,
        "dy": -1
    },
    "right": {
        "dx": 0,
        "dy": 1
    },
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
        if letter == "X":
            # print(f"# Debug: Found Letter X at {xCord}, {yCord}")
            for direction, value in directions.items():
                # print(f"# DEBUG: Start looking in direction {direction}")
                if xCord < 3 and "up" in direction.lower():
                    # print("# xCord < 3 and up in direction")
                    continue
                if xCord > len(mapStruktur) -4 and "down" in direction.lower():
                    # print(f"# xCord > len of mapStruktur -3 => {len(mapStruktur) - 4} and down in direction")
                    continue
                if yCord > len(line) -4 and "right" in direction.lower():
                    # print("# yCord > len(line)-3 and right in direction")
                    continue
                if yCord < 3 and "left" in direction.lower():
                    # print("# yCord < 3 and left in direction")
                    continue
                # print(xCord + value["dx"], ", ", yCord + value["dy"])
                if not mapStruktur[xCord + value["dx"]][yCord + value["dy"]] == "M":
                    continue
                if not mapStruktur[xCord + value["dx"]*2][yCord + value["dy"]*2] == "A":
                    continue
                if not mapStruktur[xCord + value["dx"]*3][yCord + value["dy"]*3] == "S":
                    continue
                # print(f"# DEBUG: Found Match counter + 1")
                counter += 1

print(counter)
