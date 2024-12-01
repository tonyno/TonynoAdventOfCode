import re

list1 = []
set2 = {}
with open('day1.txt', 'r') as f:
    for item in f:
        columns = re.split(r'\s+', item)
        if len(columns) >= 2:
            list1.append(int(columns[0]))
            s = int(columns[1])
            set2[s] = set2.setdefault(s, 0) + 1

list1.sort()

difference = sum(abs(value1 * set2.get(value1, 0))
                 for index, value1 in enumerate(list1))
print("List1 length: ", len(list1), "\nList2 length: ",
      len(set2), "\nScore: ", difference)
