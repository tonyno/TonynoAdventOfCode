f = open('day2.txt')
print(sum([max(splittedRow)-min(splittedRow) for splittedRow in [list(map(int, row.strip().split('\t'))) for row in f]]))
f.close()

def findIt(arr):
    for a in arr:
        for b in arr:
            if (a != b and (a % b == 0 or b % a == 0)):
                print(a,b,a/b)
                return a/b
    return 0
f = open('day2.txt')
print([findIt(splittedRow) for splittedRow in [sorted(map(int, row.strip().split('\t'))) for row in f]])
f.close()