import sys
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    x = int(input())
    if not x == 0:    
        nums.append(x)
print(round(100/min(nums)))