file = open("DATA11.txt")
gg = file.read().split()
for i in range(10):
    n =gg[i]
    x = len(n)
spot1 = [i for i in range(x-1,0,-1) if n[i] == n[0]]
spot2 = [i for i in range(x-1) if n[i] == n[x-1]]
def isPal(s):
    return s == s[::-1]
m1 = 1
for a in spot1:
    if isPal(n[:a]) > m1:
        m1 = a
        
for a in spot2:
    if isPal(n[a:x+1]) > m1:
        m1 = a
        
print(m1)