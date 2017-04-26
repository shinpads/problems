n = int(input())
m = int(input())
distracts = {i: [] for i in range(1,n+1)}
v = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    distracts[a].append(b)
    v[b]+=1
count = 0    
q = []
for i in range(1,n+1):
    if v[i] == 0:
        q.append(i)
        count+=1
        
while len(q) != 0:
    cur = q.pop(0)
    for con in distracts[cur]:
        v[con] -= 1
        if v[con] == 0:
            q.append(con)
            count+= 1
            
if count == n: print("Y") 
else: print("N")
        

    