import sys
input = sys.stdin.readline
n,m = map(int,input().split())
choice = {}

isnerd = [False for i in range(m+1)]
choice[0] = list(map(int,input().split()))[1:]

for i in choice[0]:
    isnerd[i] = True
    
for i in range(n-1):
    vals = list(map(int,input().split()))[1:]
    vals = [x for x in vals if isnerd[x]]
    choice[i+1] = vals


tot = len(choice[0])
q = [(n-1,set())]
tmin = 999 
while len(q) > 0:
    cur = q.pop(0)
    n = cur[0]
    t = cur[1]
    if n == 0:
        #print(t)
        tmin = min(tmin, tot-len(t)) 
        continue  
    else:
        f = False
        for y in choice[n]:
            f = True            
            cop = set(t)
            cop.add(y)
            q.append((n-1,cop))
        if f == False:
            q.append((n-1,set(t)))

else: print(tmin)