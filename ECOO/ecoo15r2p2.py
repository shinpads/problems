lw = input().split()
l = int(lw[0])
w = int(lw[1])
b = []
for i in range(l):
    n = list(input())
    b.append(n)
    
s = [list(b)]
while s != []:
    curb = s.pop()

def doSwap(xy, ad, curb):
    if curb[xy[0]][xy[1]] == 'X':
        curb[xy[0]][xy[1]] = 'O'
        curb[xy[0]+ad[0]][xy[1]+ad[1]] = 'X'
    else:
        curb[xy[0]][xy[1]] = 'X'
        curb[xy[0]+ad[0]][xy[1]+ad[1]] = 'O'
    for i in range(w-2):
        cTotal = 1
        while curb[i+1][xy[1]] == curb[i][xy[1]]:
            cTotal += 1
            if i < w-2:
                i+=1
            else:
                break
        if cTotal >= 3:
           for g in range(i-cTotal+1,i+1):
               curb[g][xy[1]] = '-'        
        
    s.append(list(curb))
       
for y in range(l-1):
    for x in range(w-1):
        trySwap = set([])
        cur = curb[x][y]
        if cur == curb[x+1][y]:
            if x < w-2:
                trySwap.add((x+2,y))
            if x > 0:
                trySwap.add((x-1,y))
        if cur == curb[x][y+1]:
            if y < l-2:
                trySwap.add((x,y+2))
            if y > 0:
                trySwap.add((x,y-1))
        for t in trySwap:
            xx,yy = t[0],t[1]
            tn = curb[xx][yy]
            if tn == 'X':
                tn = 'O'
            elif tn == 'O':
                tn = 'X'
            if xx < w-1:
                if curb[xx+1][yy] == tn:
                    doSwap((xx,yy),(1,0),list(curb))
            if xx > 0:
                if curb[xx-1][yy] == tn:
                    doSwap((xx,yy),(-1,0),list(curb))
            if yy < l - 1:
                if curb[xx][yy+1] == tn:
                    doSwap((xx,yy),(0,1),list(curb))
            if yy > 0:
                if curb[xx][yy-1] == tn:
                    doSwap((xx,yy),(0,-1),list(curb))
            
        
    
    