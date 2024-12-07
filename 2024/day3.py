import re

with open('day3.txt', 'r') as f:
    print("Sum: ", sum(int(m.group(1)) * int(m.group(2)) \
          for m in re.finditer(r'mul\((\d+),(\d+)\)', f.read())))

    