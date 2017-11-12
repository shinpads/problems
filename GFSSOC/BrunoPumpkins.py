N = int(input())
T = int(input())
left = []
right = []
for i in range(N):
    x = int(input())
    if x < 0:
        left.append(abs(x))
    else: right.append(abs(x))
right.sort()
left.sort()
right.insert(0,0)
left.insert(0,0)
dp = [[-1 for i in range(N+1)] for i in range(N+1)] #dp[l][r]

def solve(l,r,p):
    #solve given have searched from -l to r and still needing p more pumpkins
    if p == 0:
        return 2*min(left[l],right[r]) + max(left[l],right[r])
    if dp[l][r] != -1: return dp[l][r]
    ans = []
    if r < len(right)-1:
        ans.append(solve(l,r+1,p-1))
    if l < len(left)-1:
        ans.append(solve(l+1,r,p-1))
    dp[l][r] = min(ans)
    return dp[l][r]

print(solve(0,0,T))
