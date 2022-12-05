#filename = '.\\input\day5test.txt'
#stackCount = 3

filename = '.\\input\day5.txt'
stackCount = 9

def createStacks(lines) -> list[list[int]]:
    startIndex = 1
    jump = 4
    stacks = [ [] for r in range(stackCount) ]

    lines.reverse() # reverse the lines so the bottom of the stack gets added first
    for line in lines:
        for r in range(stackCount):
            newIndex = startIndex + (r*jump)
            if (line[startIndex + (r*jump)].strip() != ""):
                stacks[r].append(line[newIndex])
    
    return stacks

def createInstructions(lines) -> list[tuple[int, int, int]]:
    instructions = [ ]
    for line in lines:
        moveStart = 4        
        fromStart = line.index("from")
        fromEndToAdd = 5
        toStart = line.index("to")
        toEndAdd = 3

        amount = line[moveStart:fromStart]
        startLoc = line[fromStart+fromEndToAdd:toStart]
        endLoc = line[toStart+toEndAdd:]
        #subtract 1 since lists are 0 based
        inst = (int(amount.strip()), int(startLoc.strip())-1, int(endLoc.strip())-1)
        instructions.append(inst)

    return instructions

with open(filename) as f:
    lines = [ x for x in f.readlines()]
    f.close()

stacksDef = [ line for line in lines if "[" in line]
instructionsDef = [ line for line in lines if line.startswith("move")]


stacks = createStacks(stacksDef)
instructions = createInstructions(instructionsDef)
#execute instructions
for inst in instructions:
    for r in range(inst[0]):
        item = stacks[inst[1]].pop()
        stacks[inst[2]].append(item)

result = ''
for stack in stacks:
    result+= stack.pop()

print(result)


#day 2 - multiple items stay in order
#need to recreate the stack
stacksDef = [ line for line in lines if "[" in line]
stacks = createStacks(stacksDef)
for inst in instructions:
    item = ''
    for r in range(inst[0]):
        item += stacks[inst[1]].pop()
        
    item = item[::-1]
    for i in item:
        stacks[inst[2]].append(i)

result = ''
for stack in stacks:
    result+= stack.pop()

print(result)