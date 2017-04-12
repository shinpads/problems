import sys
input = sys.stdin.readline
n,q= map(int,input().split())
r = list(map(int,input().split()))

left = [r[0]]
leftamount = [1]
for i in range(1,n):
    if r[i] > left[-1]:
        left.append(r[i])
        leftamount.append(1)
    elif r[i] == left[-1]:
        left.append(r[i])
        leftamount.append(leftamount[-1]+1)
    else:
        left.append(left[-1])
        leftamount.append(leftamount[-1])
        
right = [r[-1]]
rightamount = [1]
for i in range(n-2,-1,-1):

    if r[i] > right[-1]:
        right.append(r[i])
        rightamount.append(1)
    elif r[i] == right[-1]:
        right.append(r[i])
        rightamount.append(rightamount[-1]+1)
    else:
        right.append(right[-1])
        rightamount.append(rightamount[-1])
right.reverse()
rightamount.reverse()
right = [0] + right + [0]
rightamount = [0] + rightamount + [0]
left = [0] + left + [0]
leftamount = [0] + leftamount + [0]

for i in range(q):
    a,b = map(int,input().split())
    a-=1
    b+= 1 
  
    if left[a] > right[b]:
        print(left[a],leftamount[a])
    elif left[a] == right[b]:
        print(left[a],leftamount[a] + rightamount[b])
    else:
        print(right[b],rightamount[b])
        
        
        
