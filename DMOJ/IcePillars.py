import sys
input = sys.stdin.readline
n = int(input())
w = []
d = []
for i in range(n):
    di,wi = map(int,input().split())
    d.append(di)
    w.append(wi)

def cp(x):
    if x < 0: return 0
    else: return x   
    
dp = [[0 for i in range(n)]for i in range(2)]
dp[0][0] = d[0]
dp[1][0] = cp(d[0] - w[1])
for i in range(1,n):
    a = dp[0][i-1]
    b = dp[1][i-1]        
        
    dp[0][i] = min(a + cp(d[i] - w[i-1]), b + d[i])
    if i < n-1:
        dp[1][i] = min(a + cp(d[i] - w[i-1] - w[i+1]), b + cp(d[i] - w[i+1]))    


print(dp[0][n-1])