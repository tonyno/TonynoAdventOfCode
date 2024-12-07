def word_present_on_position_and_direction(table, x, y, direction_x, direction_y):
    word = 'XMAS'
    for pos, item in enumerate(word):
        pos_y = y + direction_y*pos
        pos_x = x + direction_x*pos
        if (pos_y < 0 or pos_y >= len(table) or pos_x < 0 or pos_x >= len(table[pos_y])):
            return False # we are out of the table
        character = table[pos_y][pos_x]
        if character != item:
            return False
    return True

def find_on_position(table, x, y):
    # print(word_present_on_position_and_direction(table, 0, 0, 1, 0))
    count = 0
    for direction_x in [-1, 0, 1]:
        for direction_y in [-1, 0, 1]:
            if not(direction_x == 0 and direction_y == 0):
                if word_present_on_position_and_direction(table, x, y, direction_x, direction_y):
                    count += 1
    return count

def find_in_table(table):
    count = 0
    for y in range(len(table)):
        for x in range(len(table[y])):
            count += find_on_position(table, x, y)
    return count

table = []
with open('day4.txt', 'r') as f:
    for item in f:
        table.append(item.strip())

print("Count: ", find_in_table(table))

