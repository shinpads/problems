n,m = map(int,input().split())
pho = set(map(int,input().split()))
con = {i:set([])for i in range(n)}
for i in range(n-1):
    x,y = map(int,input().split())
    con[x].add(y)
    con[y].add(x)
    
#remove leafs:
q = [0]
v = set([])
while len(q) > 0:
    cur = q.pop()
    
    cons = list(con[cur])
    for x in cons:
        if len(con[x]) == 1 and not  cur in pho:
            con[cur].remove(x)
            con[x].clear()
        if not x in v:
            q.append(x)
            v.add(x)
    if len(con[cur]) == 1 and not cur in pho:        
        con[con[cur].pop()].remove(cur)
        con[cur].clear()
        
print(con)