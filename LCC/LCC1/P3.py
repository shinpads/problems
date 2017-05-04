for _ in range(10):
    n = int(input())
    mv = -1
    mi = 0
    vals = [int(input()) for i in range(n)]
    
    for x in range(n-1):
        if vals[x] < vals[x+1]:
            if vals[x] + vals[x+1] > mv:
                mv = vals[x] + vals[x+1]
                mi = x+1
            
    print(mi,mi+1)