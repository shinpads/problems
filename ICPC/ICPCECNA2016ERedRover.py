x = input()
best = len(x)
tr = set()
for f in range(len(x)-1):
    for e in range(f+2,len(x)):
        tr.add(x[f:e])

for n in tr:
    if len(x) - (len(n)-1)*x.count(n) + len(n)< best: 
        best = len(x) - (len(n)-1)*x.count(n) + len(n)

print(best)