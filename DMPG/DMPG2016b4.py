from math import floor, log
n = int(input())
def f(M):
    p = floor(log(M,10))+1
    return sum([int(x)**p for x in str(M)])

for _ in range(n):
    x = int(input())
    ans = set([])
    ansorder = []
    last = x
    ans.add(last)
    ansorder.append(last)
    cur = f(x)
    while True:
        
        if cur == last:
            print("Equilibrium: Bob's investment becomes $"+str(cur)+" after "+str(len(ans)-1)+" second(s)!")
            break   
           
        if cur in ans:            
            print("Instability: Loop of length "+ str(len(ans)-ansorder.index(cur)) +" encountered after " +str(ansorder.index(cur))+ " second(s)!")
            break
        
        else:
            ans.add(cur)
            ansorder.append(cur)
            last = cur
            cur = f(cur)

