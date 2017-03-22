from math import ceil
k = int(input())
n = int(input())
a = [1 for i in range(n)]

tot = 1
v = [[0 for i in range(n)] for b in range(k)]


def way(p,s):
    print(p,s)
    if p == 0 and s==p: return 1
    if p == 0 and s>0: return 0
        
    return sum([way(p-1,s-x) for x in range((s-ceil(s/p))+1)])
        
print(way(n,k))     
    