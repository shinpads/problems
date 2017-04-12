import sys
input = sys.stdin.readline
n = int(input())
l = []
cache = []
for i in range(n):
    l.append(list(map(int,input().split())))
    cache.append([-1 for i in range(n)])

def greatest(x,y):    
    if y == n-1:
        return l[y][x]
    else:
        if cache[y][x] != -1:
            return cache[y][x]
        
        cmax = -1
        for i in range(y+1):
            v = max(greatest(x,y+1),greatest(x+1,y+1))            
            if v > cmax:
                cmax = v
        cache[y][x] = l[y][x] + cmax
        return l[y][x] + cmax
print(greatest(0,0))