import sys
input = sys.stdin.readline
n = int(input())
names = input().split()
v = [1]
for i in range(1,n):
    s = names[i][0]
    if s == names[i-1][0]:
        v[-1] += 1
    else:
        v.append(1)

t = 0
for y in v:
    t += int(y*(y+1)/2)

print(t%1000000007)

