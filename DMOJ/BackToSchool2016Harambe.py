n = input()
c = 0
for x in n:
    if x == x.upper():
        c += 1
    else:
        c -= 1
if c == 0:
    print(n)
elif c > 0:
    print(n.upper())
else: print(n.lower())