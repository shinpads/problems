import itertools 
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
its = 0
for poss in itertools.permutations(range(n)):
    for ranges in itertools.permutations(rads):
        its += 1
        cval = 0
        vis = [[False for i in range(n)]for i in range(n)]
        for i in range(n):
            cpos = poss[i]
            crange = ranges[i]
            if crange == -1:continue
            if walls[cpos][i] == 0: cval = 0; break
            if cpos - crange < 0 or cpos + crange >= n or i - crange < 0 or i + crange >= n:
                cval = 0; break;
        else:
            for i in range(n):
                cpos = poss[i]
                crange = ranges[i]
                if crange == 0:
                    if not vis[cpos][i]:                    
                        cval += walls[cpos][i]
                        vis[cpos][i] = True
                else:
                    for y in range(cpos - crange, cpos + crange+1):
                        for xx in range(i-crange,i+crange+1):
                            if not vis[y][xx]:
                                cval += walls[y][xx]
                                vis[y][xx] = True

        maxvalue = max(maxvalue,cval)



print(maxvalue)
                