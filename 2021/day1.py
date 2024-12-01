
f = open('day1.txt', 'r')
lines = [int(line.strip()) for line in f.readlines()]
f.close()

increases = 0
for i in range(len(lines)-1):
    if lines[i] < lines[i+1]:
        increases += 1

print("Increases: ", increases)


increases = 0
for i in range(0, len(lines)-3):
    if lines[i]+lines[i+1]+lines[i+2] < lines[i+1]+lines[i+2]+lines[i+3]:
        increases += 1

print("Increases2: ", increases)
