d = [int(input()) for i in range(9)]
d.sort()
s =sum(d)
for x in range(0,8):
    for y in range(x+1,9):
        if s - d[x] - d[y] == 100:
            for i in (d[:x] + d[x+1:y] + d[y+1:]): print(i)
            