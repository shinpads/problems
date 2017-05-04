for _ in range(10):
    labs = set([])
    clabs = set([])
    c = 0
    for _ in range(int(input())):
        x = input()
        if x in labs:
            if x in clabs: c+=1
            else: clabs.add(x); c+=2
        else: labs.add(x)
        
    print(c)