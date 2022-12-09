#filename = '.\\input\day8test.txt'
filename = '.\\input\day8.txt'


def checkCanSeeBorder(loc: tuple[int,int], lines) -> bool:
    bottom = len(lines)-1
    right = len(lines[0])-1
    #check if this is at the edge
    if loc[0]==0 or loc[0]==right:
        return True
    if loc[1]==0 or loc[1]==bottom:
        return True

    treeHeight = int(lines[loc[1]][loc[0]])
    #check neighbours.  If it is smaller than all the neighbours dont check
    if treeHeight<=int(lines[loc[1]][loc[0]+1]) and treeHeight<= int(lines[loc[1]][loc[0]-1]) \
      and treeHeight<=int(lines[loc[1]+1][loc[0]]) and treeHeight<=int(lines[loc[1]-1][loc[0]]):
        return False


    #check up - subtract y until 0
    y = loc[1]    
    while y > 0:
        y-=1
        if treeHeight <= int(lines[y][loc[0]]):            
            break
    
    #if y bigger than the edge tree, we can see the edge
    if y==0 and treeHeight > int(lines[y][loc[0]]):
        return True

    #check down - subreact y until 0
    y = loc[1]
    while y < bottom:
        y+=1
        if treeHeight <= int(lines[y][loc[0]]):
            break
    
    #if y bigger than the edge tree, we can see the edge
    if y==bottom and treeHeight > int(lines[y][loc[0]]):
        return True


    x = loc[0]
    while x > 0:
        x-=1
        if treeHeight <= int(lines[loc[1]][x]):
            break
    
    #if x bigger than the edge tree, we can see the edge
    if x==0 and treeHeight > int(lines[loc[1]][x]):
        return True

    x=loc[0]
    while x < right:
        x+=1
        if treeHeight <= int(lines[loc[1]][x]):
            break
    
    #if x  bigger than the edge tree, we can see the edge
    if x==right and treeHeight > int(lines[loc[1]][x]):
        return True


    return False


def getSceneScore(loc: tuple[int,int], lines) -> int:
    leftScore = 0
    rightScore = 0
    upScore = 0
    downScore = 0
    
    bottom = len(lines)-1
    right = len(lines[0])-1

    #if this is at the edge, the score will be 0
    if loc[0]==0 or loc[0]==right:
        return 0
    if loc[1]==0 or loc[1]==bottom:
        return 0
    
    treeHeight = int(lines[loc[1]][loc[0]])

    #do left
    for x in range(loc[0],0,-1):
        newHeight = int(lines[loc[1]][x-1])
        if newHeight >= treeHeight:
            leftScore+=1
            break
        else:
            leftScore+=1

    #do right
    for x in range(loc[0],right,1):
        newHeight = int(lines[loc[1]][x+1])
        if newHeight >= treeHeight:
            rightScore+=1
            break
        else:
            rightScore+=1

    #do up
    for y in range(loc[1],0,-1):
        newHeight = int(lines[y-1][loc[0]])
        if newHeight >= treeHeight:
            upScore+=1
            break
        else:
            upScore+=1

    #do down
    for y in range(loc[1],bottom,1):
        newHeight = int(lines[y+1][loc[0]])
        if newHeight >= treeHeight:
            downScore+=1
            break
        else:
            downScore+=1

    return leftScore*rightScore*upScore*downScore

with open(filename) as f:
    lines = [x.strip() for x in f.readlines() if x.strip() != ""]
    f.close()

coords = set()

for y in range(len(lines)):
    for x in range(len(lines[0])):        
        if checkCanSeeBorder( (x, y), lines):
            coords.add( str(x) + "," + str(y))

print(coords)
print(len(coords))

scores = [ ]
highScore = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
            score = getSceneScore((x, y), lines)
            if score > highScore:
                highScore = score
            scores.append( (x,y,score))

print(scores)
print(highScore)