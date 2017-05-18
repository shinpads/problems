ans = []
for i in range(1024,0,-2):
    ans.append(str(i))
    ans.insert(0,str(i-1))
    
for x in ans: print(x)