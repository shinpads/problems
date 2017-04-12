n = int(input())
hts = [int(input())]
for i in range(n-1):
    c = int(input())
    if c > hts[-1]:
        hts.append(c)
    else: hts.append(hts[-1])
    
print(hts)
    