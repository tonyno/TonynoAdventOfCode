MAP = [] # just for debugging purposes
max_x = 0
max_y = 0

antinodes = set()

class Antenna:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def put_antinode(self, second):
        global antinodes, max_x, max_y
        print("Putting antinode for {} and {}".format(self, second))
        new_x = self.x + (self.x - second.x)
        new_y = self.y + (self.y - second.y)
        if (new_x >= 0 and new_y >= 0 and new_x <= max_x and new_y <= max_y):
            MAP[new_y][new_x] = '#'
            antinodes.add((new_x, new_y))

    def __repr__(self):
        return "Antenna({}, {})".format(self.x, self.y)

ANTENNAS = {}

with open('day8.txt', 'r') as f:
    for y, row in enumerate(f):
        MAP.append(list(row.strip()))
        for x, item in enumerate(row.strip()):
            if item != '.':
                ANTENNAS.setdefault(item, [])
                ANTENNAS[item].append(Antenna(x, y))
            max_x = x
            max_y = y


print(ANTENNAS)
print("Max: {}, {}".format(max_x, max_y))
for antenna in ANTENNAS:
    print("==={}===".format(antenna))
    for first in range(len(ANTENNAS[antenna])):
        for second in range(len(ANTENNAS[antenna])):
            if first != second:
                ANTENNAS[antenna][first].put_antinode(ANTENNAS[antenna][second])

print("\n".join("".join(row) for row in MAP))

print("Total antinodes: {}".format(len(antinodes)))


