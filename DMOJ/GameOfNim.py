import sys
input = sys.stdin.readline
n = int(input())
s = [int(input()) for i in range(n)]
def getreq(x):
    ans = 0
    for a in x:
        ans = ans ^ a
    return ans

def doturn():
    for i in range(n):
        if not s[i] == 0:
            v = getreq(list(s[:i]+s[i+1:]))
            if v <= s[i] and v != 0:
                print(i+1,s[i]-v)
                sys.stdout.flush()
                s[i] = v 
                break
def dobadguyturn():
    p,x = map(int,input().split())
    if p == x == 0:
        return -1
    s[p-1] -=x


if getreq(s) == 0:
    print(1,0)
    sys.stdout.flush()
    dobadguyturn()        
while True:
    doturn()
    if dobadguyturn() == -1: break
