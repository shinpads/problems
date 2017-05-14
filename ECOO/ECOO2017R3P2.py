import sys
input = sys.stdin.readline
for _ in range(10):
    n = int(input())
    dat = {}
    peeps = []
    for i in range(n):
        peeps.append(list(map(int,input().split("."))))
    count = 1
    

    for p in peeps:
        for i in range(len(p)-1,-1,-1):
            try:
                n = tuple(p[:i])
                if dat[n] < p[i]:
                    count += p[i] - dat[n]
                    dat[n] = p[i]
            except:
                dat[n] = p[i]
                count+=p[i]
                
    print(count%1000000007)