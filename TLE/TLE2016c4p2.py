from math import ceil, sqrt
l,w = map(int,input().split())
n = int(input())
x,y = 0,0
if ceil(sqrt(n) > min(l,w)):
    x = min (l,w)
    y = ceil(n/x)

else:
    x = ceil(sqrt(n))
    y = x
    if(x*(y-1)) >= n:
        y-=1
  
print((x+y) + (y-1) + (x-((x*y)%n)) + ((x*y)%n) + 1)