
filename = '.\\input\day11test.txt'
#filename = '.\\input\day11.txt'

def executeOperation(opPair: tuple[str,str], value: int) -> int:
    if opPair[0] == "*":
        if opPair[1] == "old":
            return value ** 2
        else:
            multiplier = int(opPair[1])
            return value * multiplier            
    else:
        multiplier = int(opPair[1])
        return value + multiplier



def getMonkeys(lines):
    monkeys = []
    for r in range(0,len(lines), 6):
        monkeyLines = lines[r:r+6]
        monkey = { }
        monkey["id"] = monkeyLines[0].strip()
        monkey["carrying"] = [int(i.strip()) for i in monkeyLines[1][18:].split(",")]    
    
        opPair = monkeyLines[2][23:].split(" ")
        monkey["op"] = (opPair[0].strip(),opPair[1].strip())
        
        monkey["test"] = int(monkeyLines[3][21:].strip())
        monkey["trueTarget"] = int(monkeyLines[4][29:].strip())
        monkey["falseTarget"] = int(monkeyLines[5][30:].strip())

        monkey["inspectCount"] = 0

        monkeys.append(monkey)
    
    return monkeys

with open(filename) as f:
    lines = [x for x in f.readlines() if x.strip() != ""]
    f.close()

monkeys = getMonkeys(lines)

worryDivider = 3
for round in range(0,20):
    for monkey in monkeys:
        for item in monkey["carrying"]:
            monkey["inspectCount"]+=1
            newWorryLevel = executeOperation(monkey["op"], item)            
            newWorryLevel = int(newWorryLevel / worryDivider)

            if newWorryLevel % monkey["test"] == 0:
                monkeys[monkey["trueTarget"]]["carrying"].append(newWorryLevel)
            else:
                monkeys[monkey["falseTarget"]]["carrying"].append(newWorryLevel)
        monkey["carrying"] = [ ]

print(monkeys)

counts = [m["inspectCount"] for m in monkeys]
counts.sort()

highestTwo = counts[-2:]
print(highestTwo)

monkeyBusiness = 1
for mb in highestTwo:
    monkeyBusiness*=mb
print(monkeyBusiness)


#Part 2
monkeys2 = getMonkeys(lines)
for round in range(0,20):
    for monkey in monkeys2:
        for item in monkey["carrying"]:
            monkey["inspectCount"]+=1
            newWorryLevel = executeOperation(monkey["op"], item)

            if newWorryLevel % monkey["test"] == 0:                
                monkeys2[monkey["trueTarget"]]["carrying"].append(1)
            else:
                monkeys2[monkey["falseTarget"]]["carrying"].append(newWorryLevel)
        monkey["carrying"] = [ ]

print(monkeys2)


counts = [m["inspectCount"] for m in monkeys2]
counts.sort()

highestTwo = counts[-2:]
print(highestTwo)

monkeyBusiness = 1
for mb in highestTwo:
    monkeyBusiness*=mb
print(monkeyBusiness)