import sys
from math import floor
input = sys.stdin.readline
n = int(input())
lens = input().split()
lens = [int(x) for x in lens]

maxCount = 0
nbig = 0
lens.sort()

allsums = set([])
a = 0
b = n-1
count = 0
for x in range(n):
    for y in range(x+1,n):
        allsums.add(lens[x]+lens[y])
for trySum in allsums:
    a = 0
    b = n-1
    count = 0
    while(a<b):        
        sum = lens[a]+lens[b]        
        if sum == trySum:
            count+=1
            a+=1
            b-=1
        else:
            if sum < trySum:
                a+=1
                while lens[a] == lens[a-1]:
                    a+=1
            else:
                b-=1
                while lens[b] == lens[b+1]:
                    b-=1
    #print(trySum,count)
    if count>maxCount:
        nbig = 1
        maxCount= count
        if count == floor(n/2):
            break
    elif count == maxCount:
        nbig+=1
        
print(maxCount,nbig)