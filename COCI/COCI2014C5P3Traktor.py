import sys
input = sys.stdin.readline
n,k = map(int,input().split())
countx = [0 for i in range(100001)]
county = [0 for i in range(100001)]
dl = [0 for i in range(200002)]
dr = [0 for i in range(200002)]
for i in range(n):
    x,y = map(int,input().split())
    countx[x] += 1
    county[y] += 1
    dr[x+y] += 1
    dl [x-y + 100001]+=1
    if max(countx[x],county[y],dr[x+y],dl[x-y+100001]) >= k:
        print(i+1); break
else:
    print(-1)
    