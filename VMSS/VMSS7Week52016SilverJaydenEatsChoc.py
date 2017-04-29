n = int(input())
x,y,z = map(int,input().split())
bars = [x,y,z]
bars.sort()
dp = [-1 for i in range(n+1)]
dp[n] = 0
for i in range(n-1,-1,-1):
    for t in bars:
        if i+t > n: break
        if dp[i+t] != -1:
            dp[i] = max(dp[i+t]+1,dp[i])
print(dp)          
print(dp[0])