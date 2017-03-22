code = input()
code = code.lower()
alp = list("abcdefghijklmnopqrstuvwxyz")
alpall = set(alp)
alpos = {}
for x in range(len(alp)):
    alpos[alp[x]] = x
n = input()
n = n.lower()
temp = ""
for x in n:    
    if x in alpall:        
        temp+= x
n = temp
shift = [alpos[x] for x in code]
n = list(n)
for i in range(len(n)):
    pos = i % len(shift)        
    n[i]=alp[(alpos[n[i]] + shift[pos])%26]
    
print(("".join(n)).upper())
    