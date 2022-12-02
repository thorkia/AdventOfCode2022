
filename = '.\\input\day1.txt'

with open(filename) as f:
    lines = [int(x.strip) for x in f.readlines()]
    f.close()

elves =  [ ]
currentElf = 0
elves.append(0)

for line in lines:
    if line.strip() == "":
        currentElf+=1
        elves.append(0)
    else:
        elves[currentElf] += line
#Part 1
mostCalories = max(elves)
print(mostCalories)

#Part 2
elves.sort(reverse=True)
print(sum(elves[:3]))