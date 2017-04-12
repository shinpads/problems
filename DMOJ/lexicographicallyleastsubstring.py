n = input()
c = int(input())
def gr(a,b):
    l = [a,b]
    l.sort()
    return a == l[0]
cbest = "zzzzzzzz"
for i in range(0,len(n)-c+1):
    if gr(n[i:i+c],cbest):
        cbest = n[i:i+c]
        
print(cbest)