#make a sort of prefix sum array so that p[#floors] says how many floors are taken away then just print #floors - p[#floors]
import sys
input = sys.stdin.readline
k = int(input())
y = list(map(int,input().split()))
n = int(input())
aps = []
for i in range(n):
	aps.append(int(input()))
y.sort()
amount = [0 for i in range(y[0])]
for i in range(0,k-1) :
	amount += [i+1 for ii in range(y[i+1]-y[i])]
amount += [k]
for x in aps:
  if x >= y[-1]:
    print(x - amount[-1])
  else:
    print(x - amount[x])