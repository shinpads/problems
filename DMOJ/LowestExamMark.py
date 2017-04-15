m = int(input())
g = int(input())
w = int(input())
w = w/100.0
f = False
for i in range(101):
    ans = m*(1-w) + i*w
    if ans > g or g-ans <= 0.5:
        print(i)
        f = True
        break
if not f:
    print("DROP THE COURSE")