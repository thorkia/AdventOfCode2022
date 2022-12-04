#filename = '.\\input\day4test.txt'
filename = '.\\input\day4.txt'

def isInside(area:tuple[str,str]) -> bool:
    first = area[0].split('-')
    second = area[1].split('-')

    #check if first is inside second
    if ( int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1])):
        return True
    #check if second is inside first
    elif ( int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1])):
        return True

    return False

def notOverlap(area:tuple[str,str]) -> bool:
    first = area[0].split('-')
    second = area[1].split('-')
    
    #if the start of the first is in the second we overlap
    if (int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1])):
        return False
    #if the start of the first is in the second we overlap
    elif (int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1])):
        return False
    #if we are contained in each other we overlap
    elif (isInside(area)):
        return False

    return True


with open(filename) as f:
    lines = [ (y[0],y[1]) for y in [x.strip().split(',') for x in f.readlines() if x.strip() != ""] ]
    f.close()


pairsInside = [line for line in lines if isInside(line)]

print(len(pairsInside))

pairsNotOverlap = [line for line in lines if notOverlap(line)]
overlapCount = len(lines) - len(pairsNotOverlap)

print(overlapCount)


