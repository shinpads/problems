n = int(input())
w = input()

dp = [[0 for i in range(2)]for i in range(n+1)]

for x in range(1,n+1):
    for y in range(1,n+1):
        if(w[x-1] == w[n-y]):
            dp[y][x%2] = dp[y-1][(x-1)%2] + 1
        else:
            dp[y][x%2] = max(dp[y-1][x%2],dp[y][(x-1)%2])


print(n-dp[n][n%2])
        