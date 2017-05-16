import sys
input = sys.stdin.readline
i = 1
while True:
    vals = list(map(int,input().split()))[1:]
    if vals == []: break

    dp = [[-1 for i in range(len(vals))]for i in range(len(vals))]
    def findmax(x,y):

        if x == y: return vals[x]
        if x > y: return 0
        if dp[x][y] != -1: return dp[x][y]
        ll = 0; lr = 0;
        rl = 0; rr = 0;
        # taking from right
        if vals[x] >= vals [y-1]:
            rl = 1
        else:
            rr = -1
        if vals[x+1] >= vals[y]:
            ll = 1
        else:
            lr = -1
        
        dp[x][y] = max(vals[x]+findmax(x+1+ll,y+lr),vals[y]+findmax(x+rl,y-1+rr))
        return dp[x][y]
    ez = findmax(0,len(vals)-1)
    pts = ez - (sum(vals) - ez)
    print("In game "+ str(i) + ", the greedy strategy might lose by as many as " + str(pts) + " points.")
    i+=1