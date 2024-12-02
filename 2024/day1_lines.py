import re

with open('day1.txt', 'r') as f:
    list1, list2 = zip(*list(map(lambda x: (int(x[0]), int(x[1])), (re.split(r'\s+', item) for item in f))))

list1, list2 = sorted(list(list1)), sorted(list(list2))
print(sum(abs(value1 - list2[index]) for index, value1 in enumerate(list1)))


