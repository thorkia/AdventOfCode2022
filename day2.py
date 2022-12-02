#filename = '.\\input\day2test.txt'
filename = '.\\input\day2.txt'

with open(filename) as f:
    lines = [(x.split(sep=" ")[0],x.strip().split(sep=" ")[1]) for x in f.readlines()]
    f.close()

points = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

theyWin = { 'A': 'Z', 'B': 'X' , 'C':'Y' }
theyLose = { 'A': 'Y', 'B': 'Z', 'C':'X' }

score = 0
for line in lines:
    if theyWin[line[0]] == line[1]: #you lose - 0 points
        score +=0
    elif theyLose[line[0]] == line[1]: #you win - 6 points
        score +=6 
    else:
        score +=3
    
    score+= points[line[1]]

print(score)

score2 = 0
for line in lines:
    if line[1] == 'X': #you need to lose
        score2+=points[theyWin[line[0]]]
    elif line[1] == 'Y': #you need to draw
        score2+=points[line[0]] #draw means we can use the point from our opponent
        score2+=3 #add draw points
    else: #you need to win
        score2+=points[theyLose[line[0]]]
        score2+=6

print(score2)

