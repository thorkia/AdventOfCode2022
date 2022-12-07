filename = '.\\input\day7test.txt'
#filename = '.\\input\day7.txt'
            
class Directory:        
    def __init__(self, path: str) -> None:
        self.path = path
        self.files = [ ]
        self.subdir:list[Directory]

    def getSizes(self) -> dict[str,int]:
        sizes = { }
        sizes[self.path] = sum([f[1] for f in self.files])

        for dir in self.subdir:            
            for k,v in dir.getSizes():
                sizes[k] = v

        return sizes
    


with open(filename) as f:
    lines = [x for x in f.readlines()]
    f.close()

dirs = { }
paths = [ "./",  ]
dir = { "path": "".join(paths), "files": [ ] }

for line in lines[1:]: #skip the first cd since we've created it to start
    if line.startswith("$ cd"):
        if dir["path"] not in dirs.keys():
            dirs[dir["path"]] = dir
        
        if (line.split(" ")[-1].strip()==".."):
            paths.pop()
        else:
            paths.append(line.split()[-1].strip() + "/")

        dir = { "path": "".join(paths), "files": [ ] }
    
    if line[0].isdigit():
        dir["files"].append( (line.split()[1], int(line.split()[0])))

#add the last directory
dirs[dir["path"]] = dir



for d in dirs.values():
    size = sum([i[1] for i in d["files"]])
    print(d["path"] + ":" + str(size))



fileLists = [d["files"] for d in dirs.values()]
fileTotals = [ sum([fd[1] for fd in f]) for f in fileLists]

allTogether = sum( [ s for s in fileTotals if s<=100000] )

print(allTogether)

#print(dirs.keys())