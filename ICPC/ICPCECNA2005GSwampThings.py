n = int(input())
photcount = 1
while n != 0:
    countx = [0 for i in range(10001)]
    county = [0 for i in range(10001)]
    dl = [0 for i in range(20002)]
    dr = [0 for i in range(20002)]
    most = 0
    for i in range(n):
        x,y = map(int,input().split())
        countx[x] += 1; county[y]+=1;
        dl[x+y] += 1; dr[x-y+10001]+=1;
        most = max(countx[x],county[y],dl[x+y],dr[x-y+10001],most)
        if most < 4: most = 0
    print("Photo " + str(photcount) + ": " + str(most) + " points eliminated")
    n = int(input())
    photcount += 1