dict  = {}
n = int(input())
done = False
for i in range(n):
    x = input()
    if x in dict.keys():
        dict[x] += 1        
    else:
        dict[x] = 1

for i in range(n-1):
    x = input()
    if not done:
        dict[x]-=1
        if dict[x] == 0:
            del[dict[x]]
        
for x in dict.keys():
    print(x)