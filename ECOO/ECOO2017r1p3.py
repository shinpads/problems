import sys
input = sys.stdin.readline
for _ in range(10):
    n = int(input())
    h = list(map(int,input().split()))
    v = []
    for i in range(n): v.append(0)
    mi = -1; mv = 0
    for x in range(n-1):
        cutoff = -999999
        for y in range(x+1,n):
            m = (h[y] - h[x])/(y-x)
            if m > cutoff:
                v[x] += 1
                v[y] += 1
                if v[x] > mv:
                    mv = v[x]
                    mi = x+1
                cutoff = m
    print(mi)
