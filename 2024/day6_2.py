import copy

MAP = []

x = 0
y = 0
direction_xy = (0, -1)
original_path_locations = set()



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
    global MAP, x, y, direction_xy, original_path_locations
    while x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        MAP[y][x] = 'X'
        original_path_locations.add((x,y))
        while save_get(x + direction_xy[0], y + direction_xy[1]) == '#':
            turn_right()
        x, y = x + direction_xy[0], y + direction_xy[1]


def is_deadlock():
    global MAP, x, y, direction_xy, original_path_locations
    existing_directions = set()
    while x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        MAP[y][x] = 'X'
        if (x, y, direction_xy) in existing_directions:
            return True
        existing_directions.add((x, y, direction_xy))
        #print(existing_directions)
        while save_get(x + direction_xy[0], y + direction_xy[1]) == '#':
            turn_right()
        x, y = x + direction_xy[0], y + direction_xy[1]
    return False


with open('day6.txt', 'r') as f:
    original_MAP = []
    for row in f:
        row = row.strip()
        if '^' in row:
            original_y = len(original_MAP)
            original_x = row.find('^')
        original_MAP.append(list(row))
    
x = original_x
y = original_y
direction_xy = (0, -1)
MAP = copy.deepcopy(original_MAP)
circle()

print(to_string())
print(count())
print("Len:", len(original_path_locations))

deadlocks = 0
MAP = copy.deepcopy(original_MAP)
for t in original_path_locations:
    print(t)
    x = original_x
    y = original_y
    direction_xy = (0, -1)
    MAP[t[1]][t[0]] = '#'
    if is_deadlock():
        deadlocks += 1
    MAP[t[1]][t[0]] = '.'
#print(to_string())

print("Deadlocks: ", deadlocks)

# Result: 2262


