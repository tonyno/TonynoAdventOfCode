
def split_string_permutations(value):
    # Store the result
    results = []
    s = str(value)

    # Loop to split the string into two parts
    for i in range(1, len(s)):
        part1 = s[:i]
        part2 = s[i:]
        results.append((int(part1), int(part2)))

    return results

def count(summ, array):
    if len(array) == 1:
        # print(array[0], summ)
        return array[0] == summ
    if (summ != int(summ)):
        return False # division lead to non-integer number
    if (summ < 0):
        return False
    summ = int(summ)
    v1 = summ - array[-1]
    v2 = summ / array[-1]
    print("Summ: {}, array: {}, now taking: {}, v1: {}, v2: {}".format(
        summ, array, array[-1], v1, v2
    ))
    cont = False
    if (len(str(summ)) > 1):
        n = str(array[-1])
        s = str(summ)
        print("Summ: ", s, " number: ", n, " -> ", s.endswith(n))
        if s.endswith(n) and len(s) > len(n):
            v3 = int(s.removesuffix(n))
            # print("New sum: ", v3)
            cont = count(v3, array[:-1])
            # print("V3: ", v3)
    # print("+{} /{}".format(v1, v2))
    return count(v1, array[:-1]) or count(v2, array[:-1]) or cont

selected = 0
with open('day7.txt', 'r') as f:
    for item in f:
        items = list(map(lambda x:x.strip(), item.split(':')))
        
        summ = int(items[0])
        numbers = list(map(int, items[1].split(' ')))
        if count(summ, numbers):
            selected += summ

print("Result: ", selected)



