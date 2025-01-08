from enum import Enum

ARRAY = []

class Type(Enum):
    DATA = 1
    FREE = 2

class Block:
    def __init__(self, id: int, type: Type):
        self.id = id
        self.type = type

    def __repr__(self):
        return str(self.id) if self.type == Type.DATA else '.'

def print_array():
    global ARRAY
    print("".join(map(str, ARRAY)))


with open('day9.txt', 'r') as f:
    data = f.read().strip()

id = 0
for i in range(0, len(data), 2):
    for occurence in range(0, int(data[i])):
        ARRAY.append(Block(id, Type.DATA))
    if i+1 < len(data):
        for occurence in range(0, int(data[i+1])):
            ARRAY.append(Block(id, Type.FREE))
    id += 1

if ARRAY[-1].type != Type.DATA:
    raise Exception("This we don't support")

#print_array()
EMPTY = Block(-1, Type.FREE)
pos_right = len(ARRAY)-1
pos_left = 0
steps = 0
while pos_left <= pos_right:
    while ARRAY[pos_left].type == Type.DATA: pos_left += 1
    while ARRAY[pos_right].type == Type.FREE: pos_right -= 1
    #print(pos_left, pos_right)
    if pos_left < pos_right:
        ARRAY[pos_left] = Block(ARRAY[pos_right].id, ARRAY[pos_right].type)
        ARRAY[pos_right] = EMPTY

    #print_array()

SUM = 0
for index, item in enumerate(ARRAY):
    if item.type == Type.FREE: break
    #print("{} * {}".format(index, item.id))
    SUM += index * item.id

print(SUM)


