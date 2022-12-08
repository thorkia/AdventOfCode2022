#filename = '.\\input\day7test.txt'
filename = '.\\input\day7.txt'
            
class Directory:        
    def __init__(self, path: str, parent : None) -> None:
        self.path = path
        self.files = [ ]
        self.subdir:list[Directory] = [ ]
        self.parent = parent

    def getSizes(self) -> dict[str,int]:
        sizes = { }
        sizes[self.path] = sum([f[1] for f in self.files])

        for dir in self.subdir:
            subSizes = dir.getSizes()
            sizes[self.path]+= sum([s for s in subSizes.values()]) # the current folder also includes all child folder values
            for k,v in subSizes.items():
                sizes[k] = v

        return sizes
    
    def getFileSizes(self) -> int:
        size = 0
        size+=sum([f[1] for f in self.files])
        for dir in self.subdir:
            size+=dir.getFileSizes()
        
        return size
    


with open(filename) as f:
    lines = [x for x in f.readlines()]
    f.close()


rootDirectory = None
currentDirectory = None

for line in lines: #skip the first cd since we've created it to start
    if line.startswith("$ cd"):
        if line.split()[-1].strip() == "/":            
            rootDirectory = Directory(".", None)
            currentDirectory = rootDirectory
        elif line.split(" ")[-1].strip()=="..":
            currentDirectory = currentDirectory.parent
        else:
            newDir = Directory(currentDirectory.path + "/" + line.split()[-1].strip(), currentDirectory)
            currentDirectory.subdir.append(newDir)
            currentDirectory = newDir

    elif line[0].isdigit():
        currentDirectory.files.append( (line.split()[1], int(line.split()[0])) )        

sizes = rootDirectory.getSizes()

print(sizes.keys())

print([ k for k,v in sizes.items() if v<=100000 ])
print( sum([ s for s in sizes.values() if s<=100000 ]) )

#Day 2
spaceAvailable = 70000000
targetSpace = 30000000
spaceUsed = rootDirectory.getFileSizes()

freeSpace = spaceAvailable - spaceUsed

neededSpace = targetSpace - freeSpace

dirsSmaller = [ (k,v) for k,v in sizes.items() if v>=neededSpace ]

small = min( [s[1] for s in dirsSmaller])
print(small)
#print(dirs.keys())