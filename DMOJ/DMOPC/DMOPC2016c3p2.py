import sys
input = sys.stdin.readline
n,k,d = map(int,input().split())
mulv = []
for i in range(n):
    mulv.append(1)
jacks = []

for i in range(n):
    a = input().split()
    if a[0] == "T":
        jacks.append(i)
    else:
        mulv[i] = int(a[1])
        
for i in range(n-2,-1,-1):
    mulv[i] *= mulv[i+1]
for x in jacks:    
    t = mulv[x]
    if t > d:
        print("dust")
    else: print(t)