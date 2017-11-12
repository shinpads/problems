n,t = map(int,input().split())
a = list(map(int,list(input())))
atemp = [0 for i in range(n)]
for i in range(50,-1,-1):
    if((t>>i)&1): #check if ith bit is 1
        p = (1<<i)%n
        p2 = (n-p)%n
        for x in range(0,n):
            atemp[x] = a[(x+p)%n]^a[(x+p2)%n]
        for x in range(n):
            a[x] = atemp[x]
print(''.join(list(map(str,a))))
