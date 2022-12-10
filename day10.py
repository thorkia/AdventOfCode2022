#filename = '.\\input\day10test.txt'
filename = '.\\input\day10.txt'

with open(filename) as f:
    lines = [x.strip() for x in f.readlines() if x.strip() != ""]
    f.close()

checkCycle = 20
currentCycle = 0

opCycles : dict[str,int] = { "noop": 1, "add": 2 }

registerSignalStrength : list[int] = []
registerValue : int = 1

for line in lines:
    op = line if line=="noop" else "add"
    for r in range(opCycles[op]):
        currentCycle +=1 #start the operations cycle

        if currentCycle == checkCycle:            
            registerSignalStrength.append(registerValue*checkCycle)
            checkCycle+=40
    
    #add changes value only after its second op
    if op == "add":
        registerValue+=int(line[4:].strip())
    
print(registerSignalStrength)
print(sum(registerSignalStrength))

part2CurrentCycle = 1
pixels:list[str] = [ ]
spriteMiddlePosition = 1
row = 0
pixels.append("")

for line in lines:
    op = line if line=="noop" else "add"
    for r in range(opCycles[op]):                
        #each line is 40 characters long (0-39)
        if part2CurrentCycle == 41:
            part2CurrentCycle-=40
            row+=1
            pixels.append("")

        #draw the current cycle - if it overlaps, set
        drawPosition = part2CurrentCycle-1
        if abs(spriteMiddlePosition-drawPosition)<=1:
            pixels[row] += "#"
        else:
            pixels[row] += "."
        
        part2CurrentCycle +=1 #increase the cycle
                                
    #add changes value only after its second op
    if op == "add":
        #draw the after before adjusting the position
        spriteMiddlePosition += int(line[4:].strip())

for pixel in pixels:
    print(pixel)