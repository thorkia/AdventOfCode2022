#filename = '.\\input\day3test.txt'
filename = '.\\input\day3.txt'

def getChars():
    chars = [  ]

    for r in range(0,26):
        chars.append( chr(r+97)) #97 is start of lower case

    for r in range(0,26):
        chars.append( chr(r+65) ) #65 is start of upper case

    charDict = { }
    for r in range(len(chars)):
        charDict[chars[r]] = r+1
    
    return charDict

with open(filename) as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

charPoints = getChars()
priority = 0
for line in lines:
    #split the line in half
    split = int(len(line) / 2)    
    firstHalf = set(line[:split])
    secondHalf = set(line[split:])
    priority += sum([charPoints[d] for d in firstHalf.intersection(secondHalf)])
    
print(priority)

priority2 = 0
for r in range(0,len(lines),3):
    #find the intersection of all three bags
    allthree = set(lines[r])
    allthree = allthree.intersection(lines[r+1], lines[r+2])    
        
    priority2 += sum([charPoints[d] for d in allthree])

print(priority2)