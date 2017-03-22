n = int(input())
start = int(input().split()[0])
most = start
other = 0
for i in range(n-2):
    p,m = map(int,input().split())
    start -= m    
    if m > other:
        most -= m-other
        other = 0
    else:
        other -= m
    other += p

if start < 0:print(0)
else:print(start)    
print(most)

