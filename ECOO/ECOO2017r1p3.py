import sys
input = sys.stdin.readline
for _ in range(10):
    n = int(input())
    h = list(map(int,input().split()))
    v = []
    for i in range(n): v.append(0)
    
    for x in range(n-1):
        cutoff = -999999
        for y in range(x+1,n):
            #slope = rise/run
            m = (h[y] - h[i])/(y-x)
            if m > cutoff:
                v[i] += 1
                v[y] += 1
                cutoff = m
    print(max(v))
