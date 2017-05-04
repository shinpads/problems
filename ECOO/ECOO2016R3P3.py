<<<<<<< HEAD
n = int(input())
words = set()
lmax = 0
for i in range(n):
    x = input()
    if len(x) > lmax: lmax = len(x)
    words.add(x)

for i in range(10):
    count = -1   
    w = input()

    ind = 0
    while True:
        for i in range(min(ind+lmax+1,len(w)),ind,-1):
            print(w[ind:i])
            if w[ind:i] in words:
                count+=1
                ind = i
            
            
        if ind == len(w): break

            
    print(count)

    
    
=======
import sys
def readinput():
    return sys.stdin.readline()[:-1]
input = readinput
n = int(input())
words = set()
lmax = 0
lmin = 9999
for i in range(n):
  x = input()
  if len(x) < lmin: lmin = len(x)
  elif len(x) > lmax: lmax = len(x)
  words.add(x)
  
for i in range(10):
  w = input() 
  dp = [-1 for i in range(len(w)+1)]
  dp[-1] = 0
  for x in range(len(w)-1,-1,-1):
    for y in range(min(x+lmax,len(w)),x+lmin,-1):
  
      if w[x:y] in words:
        if dp[y] != -1:
          if dp[x] == -1: dp[x] = dp[y]+1
          else: dp[x] = min(dp[x],dp[y]+1)
  
  print(dp[0]-1)
>>>>>>> origin/master
