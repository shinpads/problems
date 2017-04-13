import sys
input = sys.stdin.readline
nums = int(input())
numsList = []
for i in range(nums):
    numsList.append(int(input()))
numsList.sort()
for x in numsList:
    print(x)