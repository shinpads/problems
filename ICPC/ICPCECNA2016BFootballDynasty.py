n = int(input())
names = input().split()
wins = input()

inds = [0]
longstr = 1
curstr = 1
for i in range(1,len(wins)):
    if wins[i] == wins[i-1]:
        curstr+=1
    else:
        if curstr == longstr: inds.append(i-curstr)
        if curstr > longstr: inds = [i-curstr]; longstr = curstr       
        curstr = 1
    if i == len(wins)-1:
        if curstr == longstr: inds.append(i-curstr+1)
        if curstr > longstr: inds = [i-curstr+1]; longstr = curstr  
try:
    if inds[0] == inds[1]:
        inds.pop(0)
except: pass
indzero = False
if inds[0] == 0: indzero = True       
ans = []
ansstreak = 0
anscol = ''

white = [names[0] , names[2]] #off, def
black = [names[1] , names[3]] #off, def 

q = names[4:]




count = 0
for x in wins:
    #print(white,black,q,x)
    if count == inds[0]:
        inds.pop(0)
        if x == 'W':
            ans.append(list(white)) 
        else: ans.append(list(black))  
    if len(inds) == 0: break
    
    if x == 'W':
        white.reverse()
        q.append(black.pop())
        black.insert(0,q.pop(0))
    elif x == 'B':
        black.reverse()
        q.append(white.pop())
        white.insert(0,q.pop(0))


    count+=1
done = set()

if indzero: ans[0].reverse()
for x in ans:
    a = [x[1] , x[0]]
    if not tuple(a) in done:
        print(' '.join(a))
        #done.add(tuple(a))      
        
        