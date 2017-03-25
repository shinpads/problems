import sys
input = sys.stdin.readline
n,m = map(int,input().split())
pho = set(map(int,input().split()))
con = {i:set([])for i in range(n)}
for i in range(n-1):
    x,y = map(int,input().split())
    con[x].add(y)
    con[y].add(x)

# Remove leaves from tree to ensure that all the leaves are resturants
v = set([])
def removeLeaves(cur):       
    cons = list(con[cur])
    if not cur in pho:
        if len(con[cur]) == 1:
            con[con[cur].pop()].remove(cur)
            con.pop(cur)
           
    for x in cons:
        if not x in v:            
            v.add(x)
            removeLeaves(x)
    
    if not cur in pho:
        if cur in con.keys():        
            if len(con[cur]) == 1:
                con[con[cur].pop()].remove(cur)
                con.pop(cur)
            
removeLeaves(list(pho)[0])
#find total
#Find the largest eccentricity of all the pho nodes
def eccen(node):    
    dist = [-1 for i in range(n)]
    dist[node] = 0
    def d(x):    
        for road in con[x]:
            if dist[road] == -1:
                dist[road] = dist[x]+1
                d(road)
    d(node)
    maxValue = 0
    maxIndex = node
    for i in range(len(dist)):
        if dist[i] > maxValue:
            maxValue = dist[i]
            maxIndex = i
    return(maxValue,maxIndex)

a = eccen(pho.pop())
print(2*(len(con)-1) - eccen(a[1])[0]) 
