import sys

input = sys.stdin.readline
for _ in range(10):
    n = int(input())
    s = list(set(map(int,input().split())))
    t = map(int,input().split())
    p = set([])
    dt = set([])
    
    for x in range(len(s)):
        for y in range(x,len(s)):
            p.add(s[x]*s[y])
            p.add(s[x]+s[y])
            
    
    ans ="" 
     
    for x in t:
        f = False
        for z in s:        
            if x/z in p or x-z in p:
                ans += "T"
                f = True
                break
        if f == False:
            ans+="F"
            
    print(ans)
