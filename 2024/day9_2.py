from enum import Enum

ARRAY = []

class Type(Enum):
    DATA = 1
    FREE = 2

class Block:
    def __init__(self, id: int, size: int, free_space: int):
        self.id = id
        self.type = Type.DATA
        self.size = size
        self.free_space = free_space

    def copy(self):
        b =  Block(self.id, self.size, self.free_space)
        b.type = self.type
        return b
    
    def clear(self):
        self.free_space += self.size
        self.size = 0
    
    def cut_free_space(self, cut_size: int):
        self.free_space -= cut_size
        if self.free_space < 0:
            raise Exception("Negative freesize")
        
    def set_free_space(self, free_space: int):
        self.free_space = free_space
        if self.free_space < 0:
            raise Exception("Negative freesize")
        
    def value(self, start_pos):
        summ = 0
        for i in range(0, self.size):
            #print("    {}*{}={}".format((start_pos+i),
            #      self.id, (start_pos+i) * self.id))
            summ += (start_pos+i) * self.id
        return (summ, self.size+self.free_space)


    def __repr__(self):
        return "".join(map(lambda x: str(self.id), range(0, self.size))) + \
            "".join(map(lambda x: ".", range(0, self.free_space)))

def print_array():
    global ARRAY
    print("".join(map(str, ARRAY)))

def find_free_space(size):
    global ARRAY
    for index, item in enumerate(ARRAY):
        if item.free_space >= size:
            return index
    return None

with open('day9_test.txt', 'r') as f:
    data = f.read().strip()

id = 0
for i in range(0, len(data), 2):
    free_space = int(data[i+1]) if (i+1)<len(data) else 0
    ARRAY.append(Block(id, int(data[i]), free_space))
    id += 1


print_array()
pos_right = len(ARRAY)-1
pos_left = 0
steps = 0
while pos_right > 0:
    this_size = ARRAY[pos_right].size
    loc = find_free_space(this_size)
    print(pos_right, ARRAY[pos_right], this_size, "new location: ", loc)

    if loc != None and loc < pos_right:
        new = ARRAY[pos_right].copy()
        ARRAY[pos_right].clear()
        current_free_space = ARRAY[loc].free_space
        ARRAY[loc].free_space = 0
        ARRAY.insert(loc+1, new)
        ARRAY[loc+1].free_space = current_free_space - this_size
        #print_array()

    pos_right -= 1

    #print(pos_left, pos_right)
    # if pos_left < pos_right:
    #     ARRAY[pos_left] = Block(ARRAY[pos_right].id, ARRAY[pos_right].type)
    #     ARRAY[pos_right] = EMPTY

    #print_array()

print_array()
SUM = 0
index = 0
for item in ARRAY:
    if item.type == Type.FREE: break
    summ, inc = item.value(index)
    print("SUMM: {}, INC: {}, ITEM: {}".format(summ, inc, item))
    SUM += summ
    index += inc

print(SUM)


# print(SUM)


