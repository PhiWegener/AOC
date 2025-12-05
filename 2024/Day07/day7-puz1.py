import time
st = time.process_time()
tmp = []
mapStruktur = []

# STILL NOT WORKING!!!!!!!!!!!


# Aufbau Map wobei X die senkrechte Koordinate ist und Y die Waagerechte
#       Y  0    1    2    3    4    5    6    7    8    9    10   11
#  X
#  0     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#  1     ['.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'] 
#  2     ['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'] 
#  3     ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.']
#  4     ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'] 
#  5     ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'] 
#  6     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'] 
#  7     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'] 
#  8     ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'] 
#  9     ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'] 
# 10     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'] 
# 11     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# 


with open("input/input.txt", 'r') as file:
    for line in file:
        for letter in line:
            if not letter == "\n":
                tmp.append(letter)
        mapStruktur.append(tmp)
        tmp = []

def swapChar(vector, antennas, i):
    counter = 0
    if vector["dy"]<0:
        if antennas[i][0]-(vector["dx"]*2)<0 or antennas[i][1]+(vector["dy"]*2)>=len(mapStruktur[0]):
            return counter
        if antennas[i][0]-(vector["dx"]*-1)<0 or antennas[i][1]+(vector["dy"]*-1)>= len(mapStruktur[0]):
            return counter
        charToSwap = mapStruktur[antennas[i][0]-(vector["dx"]*2)][antennas[i][1]+(vector["dy"]*2)]
        posToSwap = (antennas[i][0]-(vector["dx"]*2), antennas[i][1]+(vector["dy"]*2))
        if charToSwap == "." or charToSwap == "#":
            mapStruktur[antennas[i][0]-(vector["dx"]*2)][antennas[i][1]+(vector["dy"]*2)] = "#"
            counter += 1
        if  charToSwap == "." or charToSwap == "#":
            mapStruktur[antennas[i][0]-(vector["dx"]*-1)][antennas[i][1]+(vector["dy"]*-1)] = "#"
            counter += 1


    if vector["dy"]>0:
        if antennas[i][0]+vector["dx"]*2 >= len(mapStruktur[0]) or antennas[i][1]-vector["dy"]*2<0:
            return counter
        charToSwap = mapStruktur[antennas[i][0]+(vector["dx"]*2)][antennas[i][1]-(vector["dy"]*2)]
        posToSwap = (antennas[i][0]-(vector["dx"]*2), antennas[i][1]+(vector["dy"]*2))
        if  charToSwap == "." or charToSwap == "#":
            mapStruktur[antennas[i][0]-(vector["dx"]*2)][antennas[i][1]+(vector["dy"]*2)] = "#"
            counter += 1
        if antennas[i][0]+(vector["dx"]*-1) >= len(mapStruktur[0]) or antennas[i][1]-(vector["dy"]*-1) < 0:
            return counter
        charToSwap = mapStruktur[antennas[i][0]+(vector["dx"]*2)][antennas[i][1]-(vector["dy"]*2)]
        posToSwap = (antennas[i][0]-(vector["dx"]*2), antennas[i][1]+(vector["dy"]*2))
        if charToSwap == "." or charToSwap == "#":
            mapStruktur[antennas[i][0]-(vector["dx"]*-1)][antennas[i][1]+(vector["dy"]*-1)] = "#"
            counter += 1
    return counter

def createAntinodes(antennas):
    counter = 0
    for i in range(len(antennas)-1):
        vector = {
            "dx": antennas[i][0]-antennas[i+1][0], 
            "dy": (antennas[i][1]-antennas[i+1][1])*-1
            }
        counter += swapChar(vector, antennas, i)
        vector = {
            "dx": antennas[i-2][0]-antennas[i][0],
            "dy": (antennas[i-2][1]-antennas[i][1])
        }
        counter += swapChar(vector, antennas, i)
    return counter


listOfFrequencies = {}

for xCoord, line in enumerate(mapStruktur):
    for yCoord, frequency in enumerate(line):
        if frequency != ".":
            # print(f"# DEBUG: Found Frequency {frequency}")
            if frequency not in listOfFrequencies.keys(): 
                listOfFrequencies[frequency] = [(xCoord, yCoord)] 
            else: 
                listOfFrequencies[frequency] += [(xCoord, yCoord)]
print(f"# DEBUG: {listOfFrequencies}")
cnt = 0
for frequency in listOfFrequencies:
    cnt += createAntinodes(listOfFrequencies[frequency])
print(f"{cnt}")
for line in mapStruktur:
    print(f"{line}")