n = int(input())
dp = [-1 for i in range(2*n)]
cards = []
for i in range(n):
    a,b = map(int,input().split())
    cards.append(a); cards.append(b)
scards = [cards[i]+cards[i-1] for i in range(1,2*n-1)]

def findmax(x,y): 
    print(x,y)
    if dp[x] != -1: return dp[x]
    end = x+11
    if end >= len(cards):
        return sum(cards[x+1:])
    
    dp[x] = min([findmax(i,x) for i in range(x+end)])
    return sum(cards[y+1:x])+dp[x]

print(findmax(0,0))