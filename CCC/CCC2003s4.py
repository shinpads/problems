n = int(input())
for i in range(n):
    s = input()
    pos = set([])
    
    for x in range(len(s)):
        for y in range(x,len(s)+1):
            pos.add(s[x:y])
        
    print(len(pos))