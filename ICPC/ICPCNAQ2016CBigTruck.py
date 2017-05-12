class Edge():
    def __init__(self,dest,cost):
        self.dest = dest
        self.cost = cost
class Dist():
    def __init__(self,dist,items):
        self.dist = dist
        self.items = items   
             
n = int(input())
items = list(map(int,input().split()))
items.insert(0,0)
m = int(input())
adj = [[]for i in range(n+1)]
for i in range(m):
    a,b,d = map(int,input().split())
    adj[a].append(Edge(b,d))
    adj[b].append(Edge(a,d))

dist = [Dist(9999999,0)for i in range(n+1)]

dist[1].dist = 0
dist[1].items = items[1]

v = [False for i in range(n+1)]

mindex = -1
#dijkstras algorithm
for i in range(n):
    mindex = -1
    for j in range(1,n+1):
        if (not v[j]) and (mindex == -1 or (dist[mindex].dist>=dist[j].dist)):
            if mindex == -1: mindex = j
            else:
                if dist[mindex].dist == dist[j].dist:
                    if dist[mindex].items <= dist[j].items:
                            mindex = j
                else:
                    mindex = j
            
    v[mindex] = True
    for edg in adj[mindex]:
        if dist[edg.dest].dist > dist[mindex].dist+edg.cost:
            dist[edg.dest].dist = dist[mindex].dist+edg.cost
            dist[edg.dest].items = dist[mindex].items+items[edg.dest]    
        elif dist[edg.dest].dist == dist[mindex].dist+edg.cost:
            dist[edg.dest].items = max(dist[edg.dest].items,dist[mindex].items + items[edg.dest])        

        
if not dist[n].dist == 9999999:
    print(dist[n].dist,dist[n].items)
else:
    print("impossible")
    
        
