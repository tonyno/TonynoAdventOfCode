import re

list1, list2 = [], []
with open('day1.txt', 'r') as f:
    for item in f:
        columns = re.split(r'\s+', item)
        if len(columns) >= 2:
            list1.append(int(columns[0]))
            list2.append(int(columns[1]))

list1.sort()
list2.sort()

difference = sum(abs(value1 - list2[index]) for index, value1 in enumerate(list1))
print("List1 length: ", len(list1), "\nList2 length: ", len(list2), "\nDifference: ", difference)