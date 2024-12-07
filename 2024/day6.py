MAP = []

x = 0
y = 0
direction_xy = (0, -1)

def turn_right():
    global direction_xy
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current_index = directions.index(direction_xy)
    direction_xy = directions[(current_index + 1) % len(directions)]

def save_get(x, y):
    if x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        return MAP[y][x]
    return None

def to_string():
    global MAP
    return ("\n".join("".join(row) for row in MAP))

def count():
    global MAP
    return to_string().count("X")

def circle():
    global MAP, x, y, direction_xy
    while x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        MAP[y][x] = 'X'
        while save_get(x + direction_xy[0], y + direction_xy[1]) == '#':
            turn_right()
        x, y = x + direction_xy[0], y + direction_xy[1]

with open('day6.txt', 'r') as f:
    for row in f:
        row = row.strip()
        if '^' in row:
            y = len(MAP)
            x = row.find('^')
        MAP.append(list(row))

circle()

print(to_string())
print(count())






def test_turn_right():
    global direction_xy
    direction_xy = (0, -1)
    turn_right()
    assert direction_xy == (1, 0)
    turn_right()
    assert direction_xy == (0, 1)
    turn_right()
    assert direction_xy == (-1, 0)
    turn_right()
    assert direction_xy == (0, -1)
    turn_right()
    assert direction_xy == (1, 0)

#           (0, -1)
#  (-1, 0)           (1, 0)
#           (0, 1)