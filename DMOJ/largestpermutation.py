n,k = map(int,input().split())
index = [0 for i in range(n+1)]
nums = list(map(int,input().split()))
nums.reverse()
for i in range(n):
    index[nums[i]] = i
    
moves = 0
for i in range(n,0,-1):
    if index[i] != i-1:
        sw = nums[i-1]
        nums[i-1] = i
        moves += 1
        ni = index[i]
        index[i] = i-1
        nums[ni] = sw
        index[sw] = ni
    if moves == k: break

nums.reverse()
nums = [str(x) for x in nums]
print(' '.join(nums))
        
    
