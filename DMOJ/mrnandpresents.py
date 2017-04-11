import sys
input = sys.stdin.readline
from collections import deque
q = deque()
v = {}
id = 0
for i in range(int(input())):
    a = input().split()
    n = int(a[1])
    a = a[0]
    if a == "F":
        q.appendleft((n,id))
        v[n] = id
    elif a == "E":
        q.append((n,id))
        v[n] = id
    else:
        v[n] = -1
    id += 1
for x in q:
    if x[1] == v[x[0]]:
        print(x[0])