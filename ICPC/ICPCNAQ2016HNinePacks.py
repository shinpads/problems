import sys
input = sys.stdin.readline
dogs = list(map(int,input().split()))[1:]
buns = list(map(int,input().split()))[1:]
n = len(dogs)
m = len(buns)

maxam = min(sum(dogs),sum(buns))+1


dpbuns = [-1 for i in range(maxam)];dpbuns[0] = 0
dpdogs = [-1 for i in range(maxam)];dpdogs[0] = 0
for x in dogs:
    dpdogs[x] = 1
for x in buns:
    dpbuns[x] = 1
    
for i in range(1,maxam):
    if dpbuns[i]!=-1:
        dpbuns[dpbuns[i]+]

