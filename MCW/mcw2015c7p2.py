import sys
input = sys.stdin.readline
f,r = map(int,input().split())
cds = []
for i in range(f):
    x = input().split()
    x[0] = int(x[0])
    for i in range(1,r):
        x[i] = int(x[i]) +x[i-1]
    cds.append(x)
for i in range(int(input())):
    a,b,c = map(int,input().split())  
    if a == 1:
        print(cds[c-1][b-1])
    else:  
        print(cds[c-1][b-1] - cds[c-1][a-2