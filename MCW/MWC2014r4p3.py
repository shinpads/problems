nq = input().split()
n = int(nq[0])
q = int(nq[1])
isSalt = set([])
atx = {}
aty = {}
for i in range(n):
    x = input().split()
    isSalt.add((x[0],x[1]))
    if x[0] in atx:
        atx[x[0]] +=1
    else: atx[x[0]] = 1
    if x[1] in aty:
        aty[x[1]] +=1
    else: aty[x[1]] = 1
    
for i in range(q):
    x = input().split()
    if x[0] == '1':
        if (x[1],x[2]) in isSalt:
            print("salty")
        else:
            print("bland")
    elif x[0] == '2':
        if x[1] == 'X':
            if x[2] in atx:
                print(atx[x[2]])
            else: print(0)
        else:
            if x[2] in aty:
                print(aty[x[2]])
            else: print(0)
        