import sys
input = sys.stdin.readline
t = int(input())
n = int(input())
parts = [[] for i in range(t+1)]
for i in range(n):
    c,v,ty = map(int,input().split())
    parts[ty].append((c,v))
    
for i in range(t+1):
    parts[i].sort(key = lambda x: x[0])
parts[1].sort(key = lambda x: x[1])
parts[1].reverse()
b = int(input())

dp = [[-1 for i in range(t+1)] for ii in range(b+1)]



def findmax(typ,money):
    #print(typ,money)
    if dp[money][typ] != -1:
        return dp[money][typ]
    
    if typ == 1:
        for i in parts[1]:
            if money - i[0] >= 0:
                return i[1]
              

        return -1

    
    val = -1
    for i in parts[typ]:
        if money - i[0] >= 0:
            valc = findmax(typ-1,money-i[0]) + i[1]
            val = max(val,valc)
        else: break
    
    dp[money][typ] = val
    return val

print(findmax(t,b))
        
            