n = int(input())
v = []
dL = 0
dR = 0
for i in range(n):
    r,l = map(int,input().split())
    v.append((r,l))
dL = n - v[n-1][0]
dR = dL + v[n-1][1] - v[n-1][0]   
for i in range(n-2,-1,-1):

    # cost to get to left is min(difference between previous left and left plus cost to get to previous left, difference between previous right and left plus cost to get to previous right)
    cl = min(abs(v[i][0] - v[i+1][0]) + dL, abs(v[i][0] - v[i+1][1]) + dR)
    cr = min(abs(v[i][1] - v[i+1][0]) + dL, abs(v[i][1] - v[i+1][1]) + dR)    
    clen = v[i][1] - v[i][0] + 1
    
    dL = cr + clen  #distance to get to left is distance to get to right + distance to span interval
    dR = cl + clen

print(dL + v[0][0]-1)



