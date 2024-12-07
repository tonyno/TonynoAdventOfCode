def safe_get(table, pos_x, pos_y):
    if (pos_y < 0 or pos_y >= len(table) or pos_x < 0 or pos_x >= len(table[pos_y])):
        return None # we are out of the table
    return table[pos_y][pos_x]

def check_direction(table, x, y, direction_x, direction_y, letters):
   return safe_get(table, x + direction_x, y + direction_y) == letters[0] \
    and safe_get(table, x - direction_x, y - direction_y) == letters[1]


def find_on_position_of_A(table, x, y):
    count = 0
    if check_direction(table, x, y, 1, 1, 'SM') or check_direction(table, x, y, 1, 1, 'MS'):
        count += 1
    if check_direction(table, x, y, -1, 1, 'SM') or check_direction(table, x, y, -1, 1, 'MS'):
        count += 1   

    if count == 2:
        return 1
    return 0

def find_in_table(table):
    count = 0
    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == 'A':
                count += find_on_position_of_A(table, x, y)
    return count

table = []
with open('day4.txt', 'r') as f:
    for item in f:
        table.append(item.strip())

print("Count: ", find_in_table(table))
