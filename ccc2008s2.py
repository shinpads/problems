from math import sqrt,floor
n = int(input())
while n != 0:
    total = 2*n +3
    for y in range(1,n):
        total +=2*( 1 + 2*floor(sqrt(pow(n,2)-pow(y,2))))
    print(total)
    n = int(input())