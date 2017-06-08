import sys
def read():
    return sys.stdin.readline()[:-1]
input = read
import bisect
q = int(input())
blue = []
pink = []
gree = []

for i in range(q):
    x = input()
    if x == "NEXT":
        if len(blue) > 0:
            print("BLUE",blue.pop(0))
        elif len(pink) > 0:
            print("PINK",pink.pop(0))
        elif len(gree) > 0:
            print("GREEN",gree.pop(0))
        else:
            print("NONE")
    else:
        f,c,n = x.split();
        n = int(n)
        if c == "BLUE":
            bisect.insort(blue,n)
        elif c == "PINK":
            bisect.insort(pink,n)
        elif c == "GREEN":
            bisect.insort(gree,n)    