from collections import defaultdict
import sys
input = sys.stdin.readline
dict  = {}
dict = defaultdict(lambda:0,dict)
n = int(input())
done = False
for i in range((n*2)-1):
    x = input()
    dict[x] += 1        

for i in dict.keys():
    if dict[i]%2 ==1:
        print(i)
        break