x,y = [list(input()),list(input())]
ind = {}
a = [0 for i in range(26)]
b = [0 for i in range(26)]
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alp)):
    ind[alp[i]] = i
    
for l in x:
    a[ind[l]]+=1
for l in y:
    b[ind[l]]+=1
total = 0   
for i in range(26):
    total+=abs(a[i] - b[i])
print(total)