import itertools
n = int(input())
c = {x:set([]) for x in range(1,9)}

for i in range(n):
    u,v = map(int,input().split())
    c[u].add(v)
    c[v].add(u)
def check3():
    for x in c.keys():
        if len(c[x]) < 3:
            return False
    return True
if n < 12:
    print("Nej")
elif not check3():
    print("Nej")
else:  
    p = list(itertools.permutations([1,2,3,4,5,6,7,8],8))
    def main():
        for x in p:
            
            if x[0] in c[x[1]] and x[0] in c[x[3]] and x[0] in c[x[4]] and x[2] in c[x[1]] and x[2] in c[x[3]] and x[2] in c[x[6]] and x[5] in c[x[4]] and x[5] in c[x[6]] and x[5] in c[x[1]] and x[7] in c[x[6]] and x[7] in c[x[4]] and x[7] in c[x[3]]:
                
                return True
        return False
    
    if main(): print("Ja") 
    else: print("Nej")
