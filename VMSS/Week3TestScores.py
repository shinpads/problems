n,k = map(int,input().split())
scores = [int(input()) for x in range(n)]
scores = [x for x in scores if x> 0]
scores.sort()

if k >= len(scores): print(sum(scores))
else: print(sum(scores[len(scores)-k:]))
