import sys
input = sys.stdin.readline
m,n = map(int,input().split())
ms = list(map(int,input().split()))
ns = list(map(int,input().split()))

dp = [[0 for i in range(m+1)] for i in range(n+1)]

for x in range(1,m+1):
    for y in range(1,n+1):
        if ms[x-1] == ns[y-1]:
            dp[y][x] = dp[y-1][x-1]+1
        else:
            dp[y][x] = max(dp[y-1][x],dp[y][x-1])
    
print(dp[n][m])