import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
pho = list(map(int,input().split()))
phos = [False for i in range(n)]
for x in pho:
    phos[x] = True
con = {i:set([])for i in range(n)}
for i in range(n-1):
    x,y = map(int,input().split())
    con[x].add(y)
    con[y].add(x)

# Remove leaves from tree to ensure that all the leaves are resturants
v = [False for i in range(n)]
def removeLeaves(cur):
       
    cons = list(con[cur])
    if not phos[cur]:
        if len(con[cur]) == 1:
            con[con[cur].pop()].remove(cur)
            con.pop(cur)
           
    for x in cons:
        if not v[x]:            
            v[x] = True
            removeLeaves(x)
    
    if not phos[cur]:
        if cur in con.keys():        
            if len(con[cur]) == 1:
                con[con[cur].pop()].remove(cur)
                con.pop(cur)
        
removeLeaves(pho[0])

#find total
#Find the largest eccentricity of all the pho nodes
def eccen(node):    
    dist = [-1 for i in range(n)]
    dist[node] = 0
    maxValue = 0
    maxIndex = node
    def d(x):
        nonlocal maxValue
        nonlocal maxIndex    
        for road in con[x]:
            if dist[road] == -1:
                dist[road] = dist[x]+1
                if dist[road] > maxValue:
                    maxValue = dist[road]
                    maxIndex = road
                d(road)
    d(node)


    return(maxValue,maxIndex)

a = eccen(pho.pop())
print(2*(len(con)-1) - eccen(a[1])[0])