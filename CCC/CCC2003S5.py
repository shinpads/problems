import sys
input = sys.stdin.readline
c,r,d = map(int,input().split())
cons = {i:[] for i in range(c+1)}
ds = set([])
for i in range(r):
    x,y,z = map(int,input().split())
    cons[x].append((y,z))
    cons[y].append((x,z))
    
for i in range(d):
    ds.add(int(input()))
    
maxw =-1
v = [-1 for i in range(c+1)]
v[1] = 9999999
q = [(1,9999999)]
while len(q) > 0:
    cur = q.pop(0)

    x = cur[0]
    xw = cur[1]
    for con in cons[x]:
        if v[con[0]] >= con[1]:
            continue
        v[con[0]] = con[1]
        q.append((con[0],con[1]))

               
print(min([v[i] for i in ds]))
    
    
    
    