import sys
sys.stdin=open("DATA11.txt")
input=sys.stdin.readline
def readin():
    return sys.stdin.readline()[:-1]
input = readin

for i in range(10):
    nare = {}
    n, m = map(int, input().split())
    vals = [[-1 for i in range(n)] for i in range(m)]
    for i in range(4):
        k, v = input().split()
        nare[k] = v
    firstFloor = input()
    lol = input()
    for i in range(n):
        vals[0][i] = firstFloor[i]
    for i in range(m-1):
        for ii in range(n):
            current = str(vals[i][ii-1]) + str(vals[i][(ii+1) % n])
            vals[i+1][ii] = nare[current]
    print(''.join(vals[-1]))