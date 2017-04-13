import sys
input = sys.stdin.readline
n = input()
g = [0]
for x in n:
    if x == "G":
        g.append(g[-1]+1)
    else:
        g.append(g[-1])


q = int(input())

for i in range(q):
    a,b = map(int,input().split())
    print(g[b+1]-g[a])
    