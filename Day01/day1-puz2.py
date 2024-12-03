list1 = []
list2 = []
with open("input/input.txt", "r") as i:
    for line in i:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    simScore = 0
    for number in list1:
        simScore += number* list2.count(number)

    print(simScore)
