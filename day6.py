#filename = '.\\input\day6test.txt'
filename = '.\\input\day6.txt'

with open(filename) as f:
    lines = [x for x in f.readlines()]
    f.close()

for line in lines:
    for r in range(len(line)-4):
        unique = set(line[r:r+4])
        if len(unique) == 4:
            print(r+4) #advent of code uses 1 based arrays
            break

#part 2 - 14 character start of message
for line in lines:
    for r in range(len(line)-14):
        unique = set(line[r:r+14])
        if len(unique) == 14:
            print(r+14) #advent of code uses 1 based arrays
            break