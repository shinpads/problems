from math import floor, ceil, log, pow
import sys
input = sys.stdin.readline
def round(x):
    if ceil(x) - x <= 0.5:return ceil(x)
    else: return floor(x)
    
def getmin(x):
    y = round(log(x,2))

    return abs(pow(2,y)-x)+1 + y
    

t = int(input())
for i in range(t):
    print(int(getmin(int(input()))))