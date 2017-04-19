c,m = map(int,input().split())

dp = [[-1 for i in range(c+1)] for i in range(m)]
dp.insert(0,[0 for i in range(c+1)])



cages = [(-1,-1)]
for i in range(c):
    a,b = map(int,input().split())
    cages.append((a,b))
    
for x in range(1,c+1):
    for y in range(m,-1,-1):
        dp[y][x] = dp[y][x-1]
        if y - cages[x][1] >= 0:
            if dp[y-cages[x][1]][x-1] != -1:
                dp[y][x] = max(dp[y][x],dp[y-cages[x][1]][x-1] + cages[x][0])

m = -1               
for i in range(len(dp)):
    if dp[i][-1] > m: m = dp[i][-1]
    
print(m)
