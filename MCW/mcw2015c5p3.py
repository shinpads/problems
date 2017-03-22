import sys
input = sys.stdin.readline
m,n = map(int,input().split())
total = 0
one = set([])
am  = {}
for x in input().split():
    if x in one:
        am[x] += 1
    else:
        one.add(x)
        am[x] =1
for x in input().split():
    if x in one: 
        if am[x] > 0:
            total+= 1
            am[x] -=1
print(total)