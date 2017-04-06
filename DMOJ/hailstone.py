n = int(input())
t = 0
while not n == 1:
    t += 1
    if n%2 == 0:
        n = n/2
    else:
        n = (n*3) + 1
print(t)