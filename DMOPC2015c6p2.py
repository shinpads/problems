from math import floor
n = int(input())
totalTilt = 0
for _ in range(n):
    totalTilt += float(input())
    totalTilt = totalTilt%360 

print(totalTilt)