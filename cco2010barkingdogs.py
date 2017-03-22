import bisect
D = int(input())
wi = [-1]
for i in range(D):
    wi.append(int(input()))

adj = [[1001 for i in range(D)]for x in range(D)]
send = {i:set([]) for i in range(D+1)}
F = int(input())
for i in range(F):
    i,j = map(int,input().split())
    send[i].add(j)
T = int(input()) 
iswait = [False for i in range(D)]
iswait[1] = True
timeline = [(0,1)]
time = 0
while True:
    for x in timeline:
        if x[0] > time:
            break
        else:
           cur = timeline.pop(0)    
    time+=1
    if time == T:
        break
    



