cons = {i:set() for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
things = []
while True:
  a = input()
  if a == "**":break
  else:
    things.append(a)
    x,y = list(a)
    cons[x].add(y)
    cons[y].add(x)
  
def BFS(ex):
  xx,yy = list(ex)
  q = ['A']
  v = {i:False for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
  
  while len(q) > 0:
    cur = q.pop()
    for c in cons[cur]:
      if cur == xx or cur == yy:
          if c == xx or c == yy:
            continue
      if v[c] == False:
        q.append(c)
        v[c] = True
  return v['B']
total = 0
for t in things:
  if not BFS(t):
    total+=1
    print(t)
    
print("There are",total,"disconnecting roads.")
