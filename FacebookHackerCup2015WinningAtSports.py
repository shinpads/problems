
dp = [[0 for i in range(2001)]for i in range(2001)]
for a in range(2001):
    for b in range(a):
        if b == a-1:
            #the only possiblility is to win every game 
            dp[a][b] = 1
        if b == 0:
            # if loser doesnt win, only one possiblity
            dp[a][b] = 1
        else:
            val = 0
            if b > 0: 
                val+= dp[a][b-1]
            if a > 0:
                val += dp[a-1][b]
                
            dp[a][b] = val%1000000007

n = int(input())
for i in range(n):
    x,y = map(int,input().split('-'))
    print('Case #' + str(i+1) + ": " + str(dp[x][y]) + " " + str(dp[y+1][y]))
                
