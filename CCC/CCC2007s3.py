import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
cons = {i:-1 for i in range(10001)}
for i in range(n):
    x,y = map(int,input().split())
    cons[x] = y
vis = set([])
def getlength(x,y):
    if x == y: return 0
    else:
        if cons[x] == -1 or x in vis:
            return -1
        else:
            vis.add(x)
            v = getlength(cons[x],y)            
            if v == -1: return -1
            else: return 1+v


while True:
    vis.clear()
    a,b = map(int,input().split())
    if a == 0 and b == 0: break
    ans = getlength(a,b)
    if ans == -1: print("No")
    else: print("Yes",ans-1)

    