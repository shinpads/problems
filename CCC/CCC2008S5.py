import sys; input = sys.stdin.readline
n = int(input())


poss = [(2,1,0,2),(1,1,1,1),(0,0,2,1),(0,3,0,0),(1,0,0,1)]
dp = [[[[False for i in range(31)]for i in range(31)]for i in range(31)]for i in range(31)]

for e in range(31):
    for f in range(31):
        for g in range(31):
            for h in range(31):
                for m in poss:
                    if e >= m[0] and f >= m[1] and g >= m[2] and h >= m[3] and not dp[h-m[3]][g-m[2]][f-m[1]][e-m[0]]:
                        dp[h][g][f][e] = True


for i in range(n):  
    a,b,c,d = map(int,input().split())                  
    if dp[d][c][b][a]: print("Patrick") 
    else: print("Roland")