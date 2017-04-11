import sys
input = sys.stdin.readline
ind = {}
n,m,q = map(int,input().split())
values = list(map(int,input().split()))
values.insert(0,0)
svals = list(values)
for i in range(1,n+1):
    ind[svals[i]] = i
    svals[i] += svals[i-1]
   
for i in range(q):
    a,b = map(int,input().split())
    #print(svals[ind[b]]-svals[ind[a]-1])
    if (svals[ind[b]]-svals[ind[a]-1])/2 >= m:
        print("Enough")
    else:
        print("Not enough") 