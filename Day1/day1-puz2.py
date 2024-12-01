list1 = []
list2 = []
resultList = []
with open("input/input.txt", "r") as i:
    for line in i:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    # list1 = sorted(list1)
    # list2 = sorted(list2)
    simScore = 0
    for number in list1:
        simScore += number* list2.count(number)

    print(simScore)
