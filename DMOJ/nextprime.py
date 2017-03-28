from math import ceil,sqrt
c = int(input())
cp = 2
ct = c
if ct % 2 == 0 :
    ct += 1
def checkPrime(n):    
    for i in range(2,ceil(sqrt(n)+1)):        
        if n % i == 0:
            return False
    return True


while cp < c:   
    
    if checkPrime(ct):        
        cp = ct
    ct += 2   
print(cp)