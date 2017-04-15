def costSort(x):

    x = list(x)
    sx = list(x)
    sx.sort()
    c = 0
    ids = {}
    vals = {}
    for i in range(len(sx)):
        ids[sx[i]] = i
        vals [x[i]] = i
    for i in range(len(x)):
        if x[i] != sx[i]:
            a = sx[i]
            b = x[i]

            x[vals[a]] = b
            x[i] = a
            vals[b] = vals[a]
            vals[a] = i
            c+=1

    return c
#costSort(['DEREK', 'MEGAN', 'BRIAN', 'BOB'])

for _ in range(10):   
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    print(min([costSort(names[:x]+names[x+1:]) for x in range(n)]))

