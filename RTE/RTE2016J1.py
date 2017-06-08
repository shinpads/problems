x = ''.join(input().split())
y = 0
for i in range(1,len(x)+1):
    if str("L"*i) in x:
        y = i
print(x.count("L"),y)