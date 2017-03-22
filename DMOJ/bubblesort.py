n = int(input())
x = list(map(int,input().split()))
print(" ".join(str(c) for c in x))

while True:
    c = 0
    for i in range(n-1):
        if x[i] > x[i+1]:
            a = x[i+1]
            x[i+1] = x[i]
            x[i] = a
            c+=1
            print(" ".join(str(c) for c in x))
    if c == 0:
        break
            
        