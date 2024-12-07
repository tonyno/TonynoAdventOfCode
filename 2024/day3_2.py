import re

sum = 0
enabled = True
with open('day3.txt', 'r') as f:
    data = f.read()
    print(data)
    for m in re.finditer(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', data):
        match m.group(0):
            case "do()": enabled = True
            case "don't()": enabled = False
            case _:
                if enabled: 
                    sum += int(m.group(2))* int(m.group(3))
print("Sum: ", sum)

