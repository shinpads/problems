import sys, time
input = sys.stdin.readline
for zz in range(10):    
    n = int(input())      
    m = list(map(float,input().split()))  
    t = time.time()
    maxes = [0 for i in range(n)]
    maxv = 0
    maxi = 0
    for i in range(n-1,-1,-1):
        if m[i] > maxv:
            maxv = m[i]
            maxi = i
        maxes[i] = maxi
    print(maxes)         
    seen = [0 for i in range(n)]
    mv = 0
    mi = 0
    for i in range(n):
        c = -100000 #threshold
        for y in range(i+1,n):                        
            dif  = m[y] - m[i]
            if dif == 0:
                ratio = 0
            else:
                ratio =abs(y-i)/(dif)
            if ratio > c:
                seen[y] += 1
                seen[i] += 1
                if seen[i] > mv:
                    mv = seen[i]
                    mi = i
                c = ratio
            if y < n- 2:
                if y+1 == maxes[y+1] and m[y+1] > m[i]:
                    y = maxes[y+1]
            #print(seen,c, i ,y)
    #print(seen)
    print(mi+1, time.time()-t)
