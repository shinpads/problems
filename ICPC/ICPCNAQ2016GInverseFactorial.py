from math import log10
import sys
input = sys.stdin.readline
n = input()
if n == '0': print(1)
else:
    le = len(n)
    if le <= 10:
        n = int(n)
        x = 1
        i = 1
        while not x == n:
            i +=1
            x*=i
            
        print(i)
    else:
        cur= 0
        i = 1
        while True:
            cur+= log10(i)
            if cur <= le:
                i+=1
            else: break
        print(i-1)

