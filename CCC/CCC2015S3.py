import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
taken = [0 for i in range(g)]
total = 0
for i in range(p):
    gi = int(input())-1
    while taken[gi] > 0 and gi >= 0:
        taken[gi] += 1
        gi = gi - (taken[gi] -1)
    if gi < 0:
        break
    else:
        total += 1
        taken[gi] = 1

print(total)