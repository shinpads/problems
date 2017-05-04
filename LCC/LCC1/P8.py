for _ in range(10):
    n = int(input())
    names = [input() for i in range(n)]
    v = [1]
    for i in range(1,n):
        s = names[i][0]
        if s == names[i-1][0]:
            v[-1] += 1
        else:
            v.append(1)
    
    t = 0
    for y in v:
        t += int(y*(y+1)/2)
    
    print(t)
