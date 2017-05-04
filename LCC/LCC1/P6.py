import sys
input = sys.stdin.readline
n = 1000000
ratings = [0]
for i in range(n):
    ratings.append(int(input()) + ratings[-1])
for _ in range(10):
    a,b = map(int,input().split())
    print(int((ratings[b] - ratings[a-1]) ))
