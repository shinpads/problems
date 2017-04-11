import sys
input = sys.stdin.readline
t = int(input())
n,k,w = map(int,input().split())
nums = [int(input()) for i in range(n)]
cache = [-1 for i in range(0,sum(nums)+1)]
def findmax(x,s):
    csum = sum(x)
    if cache[csum] != -1:
        return cache[csum]
    if s == 0:
        return 0
    poss = []
    for i in range(0,len(x)-w):
        poss.append((i,sum(x[i:i+w])))
    for i in range(n-w,n):
        poss.append((i,sum(x[i:])))
        
    poss.sort(key = lambda x: x[1])
    ans = -1
    for p in poss:
        sc = p[1]
        p = p[0]
        e = p+w
        if e > n-1:
            e = n-1
        newpins = list(x)
        for i in range(p,e):
            newpins[i] = 0
        a = sc+findmax(newpins,s-1)
        if a > ans:
            ans = a
    cache[csum] = ans
    return ans
    
print(findmax(nums,k))