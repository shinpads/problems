n = int(int(input()))
w = list(input())
alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alpi = {alp[i]:i for i in range(26)}
for x in range(len(w)):
    w[x] =  alp[alpi[w[x]]-(3*(x+1) + n)]
    
print("".join(w))