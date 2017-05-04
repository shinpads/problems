n = int(input())
words = set()
lmax = 0
for i in range(n):
    x = input()
    if len(x) > lmax: lmax = len(x)
    words.add(x)

for i in range(10):
    count = -1   
    w = input()

    ind = 0
    while True:
        for i in range(min(ind+lmax+1,len(w)),ind,-1):
            print(w[ind:i])
            if w[ind:i] in words:
                count+=1
                ind = i
            
            
        if ind == len(w): break

            
    print(count)

    
    