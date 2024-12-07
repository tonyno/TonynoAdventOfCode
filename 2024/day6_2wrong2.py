from enum import Enum
import copy

MAP = []

x = 0
y = 0
direction_xy = (0, -1)
obstacle_x = 0
obstacle_y = 0

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
    return ' '

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


def is_deadlock(obstacle_position, maximum_steps):
    global MAP, x, y, direction_xy, obstacle_x, obstacle_y
    steps = 0
    #print("Obstacle position: ", obstacle_position)
    while x >= 0 and x < len(MAP[0]) and y >= 0 and y < len(MAP) and steps < maximum_steps:
        MAP[y][x] = 'X'
        
        steps += 1
        if obstacle_position == steps:
            obstacle_x = x + direction_xy[0]
            obstacle_y = y + direction_xy[1]
            if (save_get(obstacle_x, obstacle_y) in ('#')):
                # I am trying to put obstacle to place where is already obstacle,
                # so let's put it behind the corner
                turn_right()
                obstacle_x = x + direction_xy[0]
                obstacle_y = y + direction_xy[1]
            save_put(obstacle_x, obstacle_y, 'O')

        while (save_get(x + direction_xy[0], y + direction_xy[1]) in ('#', 'O')):
            turn_right()
        x, y = x + direction_xy[0], y + direction_xy[1]

    if steps == maximum_steps:
        return Result.DEADLOCK
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
ITEMS = 4 * 6000  # the value is from day6.py - for all possible directions
distinct_pos = set()
while steps < ITEMS:   
    steps += 1
    MAP = copy.deepcopy(MAP_ORIGINAL) # UFF, NEW LEARNING. MAP = MAP_ORIGINAL[:] didn't work on two dimensional array
    #print(id(MAP[0]), id(MAP_ORIGINAL[0]))
    x = original_x
    y = original_y
    direction_xy = (0, -1)
    status = is_deadlock(steps, ITEMS)  # the value is from day6.py
    if status == Result.DEADLOCK:
        print("Steps: ", steps, " Status: ", status, "\n", to_string(), "\n\n")
        deadlocks += 1
        distinct_pos.add("{}-{}".format(obstacle_x, obstacle_y))



print("Deadlocks: ", deadlocks)
print("Distinct deadlocks: ", len(distinct_pos))
# Wrong: 2146 small
# Wrong: 2810 too big
# Wrong: 2480 too high
# Deadlocks:  2496 for 6k
# Deadlocks:  2483 for 9k
# Deadlocks:  2480 for 15k

# Deadlocks:  2480
# Distinct deadlocks:  2285

# Deadlocks:  2421
# Distinct deadlocks:  2220

# Deadlocks:  2545
# Distinct deadlocks:  2344 .... too low


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