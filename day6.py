#filename = '.\\input\day6test.txt'
filename = '.\\input\day6.txt'

def startChar(message: str, windowSize: int) -> int:
    for r in range(len(message)-windowSize):
        unique = set(message[r:r+windowSize])
        if len(unique) == windowSize:
            return r+windowSize #advent of code uses 1 based arrays            
    return -1

with open(filename) as f:
    lines = [x for x in f.readlines()]
    f.close()

for line in lines:
    print(startChar(line, 4))

#part 2 - 14 character start of message
for line in lines:
    print(startChar(line, 14))