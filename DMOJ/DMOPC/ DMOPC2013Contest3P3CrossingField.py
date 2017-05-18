import sys
input = sys.stdin.readline
n,h = map(int,input().split())
vals = []
for i in range(n):
  vals.append(list(map(int,input().split())))
v = [[False for i in range(n)] for i in range(n)] 
v[0][0] = True
q = [(0,0)]
while len(q) > 0:
  x,y = q.pop()

  if x == n-1 and y == n-1:
    print("yes"); break
  for t in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    tx,ty = t

    if tx > -1 and tx < n and ty > -1 and ty < n and abs(vals[x][y] - vals[tx][ty]) <= h and not v[tx][ty]:
      q.append(t)
      v[x][y] = True
else:
  print("no")
