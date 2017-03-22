n = int(input())
B,L,D = map(int,input().split())
x = []
for i in range(3):
    x.append([int(abc) for abc in input().split()])
    
cp = [[0 for i in range(6001)]for b in range(3)]
for g in x[0]:
    cp[0][g] = 1

for h in range(n):
    for xx in x[1]:
        if xx+h <= n:
            cp[1][xx+h] += cp[0][h]
    for xx in x[2]:
        if xx+h <= n:
            cp[2][xx+h] += cp[1][h]
    for xx in x[0]:
        if xx+h <= n:
            cp[0][xx+h] += cp[2][h]
z = False     
if sum([min(x[g]) for g in range(3)]) == 0:
    z = True
for h in range(n,-1,-1):
    if cp[0][h] + cp[1][h] + cp[2][h] > 0:
        if z:
            print(0,n-h)
        else:        
            print(sum([cp[i][h] for i in range(3)]),n-h)        
        break
    
