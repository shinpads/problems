import sys; input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l,w = map(int,input().split())
    dist = [[float('inf') for i in range(l)]for i in range(w)]
    graph = [list(input()) for i in range(w)]
    
    for x in range(l):
        for y in range(w):
            if graph[y][x] == 'C':
                start = (x,y,0);
            if graph[y][x] =='W':
                end = (x,y)
    
    q = [start]
    while len(q) > 0:
        x,y,d = q.pop(0)
        if d == 59: continue
        for tx,ty in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if tx < l and tx>=0 and ty<w and ty>= 0:
                if not graph[ty][tx] == 'X':
                    if dist[ty][tx] == float('inf'):
                        q.append((tx,ty,d+1))
                    dist[ty][tx] = min(dist[ty][tx],d+1)
                    
    d = dist[end[1]][end[0]]
    if d == float('inf'):
        print('#notworth')
    else:
        print(d)
            
    
    