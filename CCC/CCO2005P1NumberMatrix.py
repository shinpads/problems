n,m = map(int,input().split())
nums = []
for i in range(m):
    nums.append(list(map(int,input().split())))
# nums[n][m] = nums[y][x]

def BFS(vals):
    v = [[False for i in range(n)] for i in range(m)]
    q = []
    for t in range(n):
        if nums[0][t] in vals:
            q.append((t,0))
    while len(q) > 0:
        x,y = q.pop()
        if y == m-1: return True
        for t in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
            tx,ty = t
            if tx >= 0 and tx < n and ty < m and ty >= 0 and not v[ty][tx]:
                if nums[ty][tx] in vals:
                    q.append(t)
                    v[ty][tx] = True
    return False
def trystuff():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                if BFS((a,b,c)):
                    print(a,b,c); return True                    
if not trystuff():
    print(-1)
    