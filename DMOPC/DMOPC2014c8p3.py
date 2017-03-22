n = int(input())
_ = input()
aset = set([])

for a in input().split():
    aset.add(a)
for b in input().split():
    if b in aset:
        n-=1
print(n)
