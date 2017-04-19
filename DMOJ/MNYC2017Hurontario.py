import sys
input = sys.stdin.readline
a,b = input().split()
for i in range(len(b)-1,-1,-1):
    if b[i] == a[-1]:
        for ii in range(i + 1):
            if b[i-ii] != a[-1 - ii]:
                break
        else:
            b = b[ii+1:]
            break

print("".join([a,b]))