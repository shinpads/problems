import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for i in range(n)]
cache = [-1 for i in range(n)]
cache[-1] = nums[-1]
def findMax(x):        
    if cache[x] != -1:
        return cache[x]    
    for i in range(x+1,n):
        if nums[i] > nums[x]:
            cval = nums[x] + findMax(i)        
            if cval > cache[x]:
                cache[x] = cval
    if cache[x] == -1:
        return nums[x]
    else:
        return cache[x]
ans = []
for i in range(n):
    ans.append(findMax(i))
    
print(max(ans))