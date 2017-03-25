import sys
input = sys.stdin.readline
n = int(input())
lengths = [0 for i in range(2002)]
total = [0 for i in range(4004)]
nums = list(map(int,input().split()))
for x in nums:
    lengths[x] +=1

for x in range(len(lengths)):
    if lengths[x] > 0:
        for y in range(x,len(lengths)):
            if x == y:
                if lengths[x] > 1:
                    total[x+y] += int(lengths[x]/2)
            else:
                total[x+y] += min(lengths[x],lengths[y])

a = max(total)
print(a,total.count(a))
