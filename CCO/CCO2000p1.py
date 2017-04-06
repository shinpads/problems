n = int(input())
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cont = {i:set([]) for i in alp}
contA = {i:set([]) for i in alp}
v = {i:False for i in alp}
done = set([])
for i in range(n):
    x = input()
    done.add(x[0])
    if x[-1].isupper():
        done.add(x[-1])        
        contA[x[0]].add(x[-1])
    else:
        cont[x[0]].add(x[-1])

def addsub(x):
    if v[x]: return
    v[x] = True    
    for i in set(contA[x]):        
        addsub(i)
        contA[x] = contA[x].union(contA[i])
done = list(done)
done.sort()

for x in done:
    addsub(x)
    for i in contA[x]:
        cont[x] = cont[x].union(cont[i])
    vals = list(cont[x])
    vals.sort()
    vals = ",".join(vals)
    print(x,"=","{"+vals+"}")


