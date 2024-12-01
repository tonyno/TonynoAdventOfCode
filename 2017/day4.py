
def validPassowrd(s): return len(set(s.split(' '))) == len(s.split(' '))
f = open('day4.txt')
print(len([row for row in f if validPassowrd(row.strip())]))
f.close()

def mySort(s): return ''.join(sorted(s))
def validPassowrd2(s): return len(set(map(mySort, s.split(' ')))) == len(list(map(mySort, s.split(' '))))
f = open('day4.txt')
print(len([row for row in f if validPassowrd2(row.strip())]))
f.close()