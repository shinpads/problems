n = int(input())
cuteness = input().split()
cuteness  = [int(x) for x in cuteness]
probs = []
for i in range(n):
    probs.append(input().split())
time = 180 - max([int(x[2]) for x in probs])
for i in range(n):
    i,p,s,t = map(int,probs[i])
    if p == 10:
        print(0)     
    elif cuteness[i-1]*t <= time:
        print(10-p)
    else:
        print("The kemonomimi are too cute!")
        
    