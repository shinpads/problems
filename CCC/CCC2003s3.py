f = int(input())
r = int(input())
c = int(input())
grid = [[0 for i in range(r+3)]for x in range(c+3)]
cid = 1
class RootID:
    def __init__(self,sid):
        self.id = sid
        
class Node:
    def __init__(self,root):
        self.parent = root
        
for i in range(r):
    line = input()
    for x in range(len(line)):
        if  line[x] == ".":
            
            #grid[i][x]
            if grid[i-1][x] == grid[i][x-1] == 0:
                grid[i][x] = Node(RootID(cid))
                cid += 1
            elif grid[i-1][x] == grid[i][x-1]:
                grid[i][x] = Node(grid[i][x-1].parent)
            elif grid[i-1][x] == 0 and grid[i][x-1] != 0:
                grid[i][x] = Node(grid[i][x-1].parent)
            elif  grid[i-1][x] != 0 and grid[i][x-1] == 0:
                grid[i][x] = Node(grid[i-1][x].parent)
            else:                
                grid[i-1][x].parent.id = grid[i][x-1].parent.id
                grid[i][x] = Node(grid[i][x-1].parent)
                
total = [0 for i in range(cid+1)]

for i in range(r):
    print("".join([str(x.parent.id//2) if not x == 0 else "0" for x in grid[i]]))

for i in range(r):
    for x in range(c):
        
        if grid[i][x] != 0:
            total[grid[i][x].parent.id] += 1

total.sort()
while total[0] == 0:
    total.pop(0)
rooms = 0
#print(total)

for i in range(len(total)-1,-1,-1):  
    
    if f - total[i] >=0:
        f -= total[i]
        rooms+=1
    else:        
        break
    
if rooms == 1:
    print(rooms,"room,",f,"square metre(s) left over")
    
else:
    print(rooms,"rooms,",f,"square metre(s) left over")

                
                