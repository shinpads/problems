import sys
sys.stdin=open("DATA21.txt")
input=sys.stdin.readline
def readin():
    return sys.stdin.readline()[:-1]
input = readin
for i in range(10):
    n = int(input())
    ma = []
    for i in range(n):
        ma.append(list(input()))
    #find s
    start = 0
    for x in range(n):
        for y in range(n):
            if ma[x][y] == "S": start = (x,y); break
    
                
    v= [[False for i in range(n)] for i in range(n)]
    doorq = []
    
    keys = 0
    tres = 0
    def bfs(st):
        global tres
        global keys
        global v
        ma[st[0]][st[1]] = "."
        v[st[0]][st[1]] = True
        q = [st]
        while len(q) > 0:
    
            cur = q.pop()
            
            cx,cy = cur
            for tr in ((cx-1,cy),(cx+1,cy),(cx,cy+1),(cx,cy-1)):
                tx,ty = tr
                if tx < n and tx >= 0 and ty < n and ty >= 0 and not v[tx][ty]:
                    v[tx][ty] = True
                    if ma[tx][ty] == "T" or ma[tx][ty] == "K" or ma[tx][ty] == ".":
                        if ma[tx][ty] == "K":
                            keys+=1
                            ma[tx][ty] = "."
                        if ma[tx][ty] == "T":
                            tres += 1
                            ma[tx][ty] = "."
                        q.append(tr)
                    elif ma[tx][ty] != "#":                  
                        doorq .append((tx,ty))
    
        # check next door
    
        for i in range(len(doorq)):
            xx,yy = doorq[i]
            if int(ma[xx][yy]) <= keys:
                bfs(doorq.pop(i)); break
                
    
    bfs(start)    
    print(tres)
    
    
    
    

    
    
    
    
    
    

