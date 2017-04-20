n,m,a,b = map(int,input().split())
cons = {i:set([]) for i in range(n+1)}
for i in range(m):
    x,y = map(int,input().split())
    cons[x].add(y)
    cons[y].add(x)

q = [a]
v = [False for i in range(n+1)]
while len(q) > 0:    
    cur = q.pop(0)
    if v[cur]: continue
    else: v[cur] = True
    if cur == b: print("GO SHAHIR!"); break
    else:
        for con in cons[cur]:
            q.append(con)
            
else:
    print("NO SHAHIR!")