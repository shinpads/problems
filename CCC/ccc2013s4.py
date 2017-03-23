import sys
input = sys.stdin.readline
n,m = map(int,input().split())
taller = {i:set([]) for i in range(n+1)}
for i in range(m):
    x,y = map(int,input().split())
    taller[x].add(y)
p,q = map(int,input().split())
v = [0 for i in range(n+1)]
def isTaller(x,y):
    if v[x] == 1:
        return 0
    if y in taller[x]:
        return 1
    
    else:
        for a in taller[x]:
            if isTaller(a,y):
                return 1
        v[x] = 1
        return 0
    
a = isTaller(p,q)
b = isTaller(q,p)
if a:
    print("yes")
elif b: print("no")
else: print("unknown")
