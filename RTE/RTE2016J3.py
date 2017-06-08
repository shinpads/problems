t = int(input())
for _ in range(t):
    n,c = map(int,input().split())
    beans = [0 for i in range(n+1)]
    donezo = [False for i in range(n+1)]
    for i in range(c):
        inp = input().split()
        if inp[0] == "A":
            a,n,x = inp; n = int(n); x = int(x);
            if not donezo[x]:
                beans[x]+=n
        else:
            a,x = inp; x = int(x)
            if a == "Q":
                print(beans[x])
            elif a == "G":
                print(sum(beans[:x+1]))
            elif a == "L":
                print(sum(beans[n-x+1:]))
            else:
                beans[x] = 0
                donezo[x] = True