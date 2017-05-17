n,q = map(int,input().split())
cons = [[] for i in range(n+1)]

def iscon(a,b):
    if len(cons[b]) == 0: return False
    v = [False for i in range(n+1)]
    q = [a]
    while len(q) >0:
        cur = q.pop()
        for x in cons[cur]:
            if x == b: return True
            if not v[x]:
                q.append(x)
                v[x] = True
    return False
    
for _ in range(q):
    a,b,c = input().split(); b = int(b); c = int(c)
    if a == 'A':
        cons[b].append(c)
        cons[c].append(b)
    else:
        if iscon(b,c):
            print('Y')
        else: print('N')
                