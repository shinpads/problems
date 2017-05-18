import sys;
sys.stdin = open('s4.4.in')
input = sys.stdin.readline
n = int(input())
t = int(input())

adj = [[-1 for i in range(n+1)]for i in range(n+1)]

for i in range(t):
    a,b,d = map(int,input().split())
    if adj[a][b] == -1:
        adj[a][b] = d
        adj[b][a] = d
    else:
        adj[a][b] = min(adj[a][b],d)
        adj[b][a] = min(adj[b][a],d)

k = int(input())
pcit = []
for i in range(k):
    pcit.append(list(map(int,input().split())))

home = int(input())    

dist = [float('inf') for i in range(n+1)]
v = [False for i in range(n+1)]
dist[home] = 0
print("DONE READING")
mindex = -1
#dijkstras algorithm
for i in range(n):
    mindex = -1
    for j in range(1,n+1):
        if (not v[j]) and (mindex == -1 or (dist[mindex]>dist[j])):
            mindex = j
    #print(mindex,dist[mindex])     
    v[mindex] = True
    for edg in range(1,n+1):
        if not adj[mindex][edg] == -1:
            if dist[edg] > dist[mindex] + adj[mindex][edg]:
                dist[edg] = dist[mindex] + adj[mindex][edg]
     

best = float('inf')        
for cit in pcit:
    c,cost = cit
    best = min(best,dist[c]+cost)
    
print(best)


    