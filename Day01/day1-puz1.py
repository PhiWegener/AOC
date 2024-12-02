list1 = []
list2 = []
resultList = []
with open("input/input.txt", "r") as i:
    for line in i:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    list1 = sorted(list1)
    list2 = sorted(list2)
    for index, number in enumerate(list1):
        diff = list1[index]-list2[index]
        if diff < 0:
            resultList.append(diff * -1)
        else: 
            resultList.append(diff)

    print(sum(resultList))
