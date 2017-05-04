import itertools 
from copy import deepcopy
import sys
input = sys.stdin.readline
n = int(input())
walls = []
for i in range(n):
    walls.append(list(map(int,input().split())))

a = int(input())
rads = list(map(int,input().split()))

for i in range(a):
    rads[i] -= 1
rads += [-1 for i in range(n-a)]
maxvalue = 0
for poss in itertools.permutations(range(n)):
    for ranges in itertools.permutations(rads):
        cval = 0
        wallc = deepcopy(walls)
        for i in range(n):
            cpos = poss[i]
            crange = ranges[i]
            if crange == -1: print(i,cpos,-1,cval);continue
            if walls[cpos][i] == 0: cval = 0; break
            if cpos - crange < 0 or cpos + crange >= n or i - crange < 0 or i + crange >= n:
                cval = 0; break;
            else:
                if crange == 0:                    
                    cval += wallc[cpos][i]
                    wallc[cpos][i] = 0
                else:
                    for y in range(cpos - crange, cpos + crange+1):
                        cval += sum(wallc[y][i-crange:i+crange+1])
                        for xx in range(i-crange,i+crange+1):
                            wallc[y][xx] = 0

        maxvalue = max(maxvalue,cval)



print(maxvalue)
                