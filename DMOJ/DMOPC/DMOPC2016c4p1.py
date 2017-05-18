import sys
input = sys.stdin.readline
n = int(input())
p = [-1 for i in range(500001)]
def ispow(x):
    
    return (x&(x-1)) == 0 and x != 0
for _ in range(n):
    nn = int(input())
    if ispow(nn):
        print("T")
    else:
        print("F")
