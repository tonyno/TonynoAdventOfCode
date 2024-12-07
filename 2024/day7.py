
def count(summ, array):
    if len(array) == 1:
        # print(array[0], summ)
        return array[0] == summ
    v1 = summ - array[-1]
    v2 = summ / array[-1]
    # print("+{} /{}".format(v1, v2))
    return count(v1, array[:-1]) or count(v2, array[:-1])

selected = 0
with open('day7.txt', 'r') as f:
    for item in f:
        items = list(map(lambda x:x.strip(), item.split(':')))
        
        summ = int(items[0])
        numbers = list(map(int, items[1].split(' ')))
        if count(summ, numbers):
            selected += summ

print("Result: ", selected)