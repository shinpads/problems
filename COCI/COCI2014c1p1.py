n = int(input())
nums = input().split()
ans = [int(nums[0])]

for i in range(1,n):
    x = int(nums[i])
    past = ans[0:i]    
    past = [int(gg) for gg in past]
    ans.append(x*(i+1) - sum(past))    
    
an = ""
for i in ans:
    an += str(i) +" "
print(an)