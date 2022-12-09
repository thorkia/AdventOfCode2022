#filename = '.\\input\day9test.txt'
filename = '.\\input\day9.txt'

def getMoveVector(dir:str) -> tuple[int,int]:
    if dir == "R":
        return (1,0)
    elif dir == "L":
        return (-1,0)
    elif dir == "U":
        return (0,1)
    else: #down is last one
        return (0,-1)

def applyVector(first:tuple[int,int], second:tuple[int,int]) -> tuple[int,int]:
    return (first[0]+second[0],first[1]+second[1])

def moveTail(headLoc:tuple[int,int], tailLoc:tuple[int,int]) -> tuple[int,int]:
    difference = (headLoc[0]-tailLoc[0], headLoc[1]-tailLoc[1]) #generate the gap
    
    #if both locations are only 1 away, then we are beside the location
    if abs(difference[0]) <= 1 and abs(difference[1]) <= 1:
        return tailLoc
    
    xVector = 0
    if difference[0] > 0:
        xVector = 1
    elif difference[0] < 0:
        xVector = -1
    
    yVector = 0
    if difference[1] > 0:
        yVector = 1
    elif difference[1] < 0:
        yVector = -1
    
    newLoc = applyVector(tailLoc, (xVector,yVector))
    #print("Head:" + str(headLoc) + " Tail:" + str(tailLoc))
    return newLoc

with open(filename) as f:
    lines:tuple[str,int] = [(x.split(sep=" ")[0],int(x.strip().split(sep=" ")[1])) for x in f.readlines() if x.strip() != ""]
    f.close()

headLoc = (0,0)
tailLoc = (0,0)
visited = set()

for dir,amt in lines:
    move = getMoveVector(dir)
    for r in range(amt):
        headLoc = applyVector(headLoc, move)
        tailLoc = moveTail(headLoc, tailLoc)
        visited.add(tailLoc)
        
print(visited)
print(len(visited))


rope = [ ]
for r in range(10):
    rope.append( (0,0) )
visitedPart2 = set()

for dir,amt in lines:
    move = getMoveVector(dir)
    for r in range(amt):
        rope[0] = applyVector(rope[0], move)
        for r in range(1,10):
            rope[r] = moveTail(rope[r-1], rope[r])
            if r == 9:
                visitedPart2.add(rope[9])

print(visitedPart2)
print(len(visitedPart2))
