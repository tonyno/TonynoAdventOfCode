from enum import Enum
import copy

MAP = []

x = 0
y = 0
direction_xy = (0, -1)

class Result(Enum):
    DEADLOCK = 1
    NO_DEADLOCK = 2
    FINAL_RUN = 3

def turn_right():
    global direction_xy
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current_index = directions.index(direction_xy)
    direction_xy = directions[(current_index + 1) % len(directions)]

def save_get(x, y):
    if x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        return MAP[y][x]
    return None

def save_put(x, y, character):
    if x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        MAP[y][x] = character

def to_string():
    global MAP
    return ("\n".join("".join(row) for row in MAP)) + "\n\n"

def count():
    global MAP
    return to_string().count("X")

def direction_character():
    global direction_xy
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    letters = '^>v<'
    current_index = directions.index(direction_xy)
    return letters[current_index]


def is_deadlock(obstacle_position):
    global MAP, x, y, direction_xy
    steps = 0
    MAP[y][x] = "X"
    #print("Obstacle position: ", obstacle_position)
    while x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP):
        if MAP[y][x] == direction_character():
            return Result.DEADLOCK
        MAP[y][x] = direction_character()
        
        steps += 1
        if obstacle_position == steps:
            save_put(x + direction_xy[0], y + direction_xy[1], 'O')


        while (save_get(x + direction_xy[0], y + direction_xy[1]) in ('#', 'O')):
            turn_right()
        x, y = x + direction_xy[0], y + direction_xy[1]

    if steps >= obstacle_position:
        return Result.FINAL_RUN
    return Result.NO_DEADLOCK


MAP_ORIGINAL = []
with open('day6.txt', 'r') as f:
    for row in f:
        row = row.strip()
        if '^' in row:
            original_y = len(MAP_ORIGINAL)
            original_x = row.find('^')
        MAP_ORIGINAL.append(list(row))

steps = 0
deadlocks = 0
status = Result.NO_DEADLOCK
while steps <= 5534: # the value is from day6.py
    steps += 1
    MAP = copy.deepcopy(MAP_ORIGINAL) # UFF, NEW LEARNING. MAP = MAP_ORIGINAL[:] didn't work on two dimensional array
    #print(id(MAP[0]), id(MAP_ORIGINAL[0]))
    x = original_x
    y = original_y
    direction_xy = (0, -1)
    status = is_deadlock(steps)
    if status == Result.DEADLOCK:
        print("Steps: ", steps, " Status: ", status, "\n", to_string(), "\n\n")
        deadlocks += 1



print("Deadlocks: ", deadlocks)
# Wrong: 2146





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


# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ....^.....
# .#.#^.....
# ........#.
# #.........
# ......#...