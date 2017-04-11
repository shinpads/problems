import sys
input = sys.stdin.readline
n,q = map(int,input().split())
ratings = list(map(int,input().split()))
for i in range(1,n):
    ratings[i] = ratings[i]+ratings[i-1]
ratings.insert(0,0)
   
for i in range(q):
    a,b = map(int,input().split())
    print(ratings[-1] - ratings[b] + ratings[a-1])