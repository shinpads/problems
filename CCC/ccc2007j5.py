import bisect
A = int(input())
B = int(input())
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
n = int(input())
for i in range(n):
    bisect.insort(motels,int(input()))
n = len(motels)
q = [[0,0,0]]
ans = 0
visited = set((0,0,0))  
while q != []:       
    cur = q.pop(0) 
    #print(cur,q)    
    if cur[1] == 7000:
        ans += 1
    else:        
               
        for i in range(cur[0],n):
            if motels[i] - cur[1] > B:
                break
            elif motels[i] - cur[1] < A:
                next
            elif motels[i] == 7000:
                ans += 1                
            else:
                q.append([i,motels[i],cur[0]])
                visited.add(tuple(cur))
   
print(ans)