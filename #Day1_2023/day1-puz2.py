resultList = []
numberAsWordsList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("input/input.txt", "r") as i:
    for line in i:
        returnstr = ""
        # lineTmp = line
        for index, number in enumerate(numberAsWordsList):
            if number in line:
                line = line.replace(number, str(index))
        print(line)
            
        for letter in line:
            # step 1
            if letter.isdigit():
                returnstr += letter
                
        # step 2
        if len(returnstr) == 2:
            # print("DEBUG: returnstr = 2")
            # print(returnstr)
            resultList.append(returnstr)
        elif len(returnstr) == 1:
            # print("DEBUG: returnstr = 1")
            returnstr += returnstr
            # print(returnstr)
            resultList.append(returnstr)
        else:
            # print("DEBUG: returnstr != 2")
            returnstr = returnstr[0] + returnstr[-1]
            # print(returnstr)
            resultList.append(returnstr)

# check output after reading file:
# print(resultList)

# make all list items to integers
result = sum(map(int, resultList))

print(result)