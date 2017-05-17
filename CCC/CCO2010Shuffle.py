
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
shuf = {i:'' for i in alp}
for i in range(27):
    shuf[alp[i]] = input()
amount = int(input())
answers = {}  
def findchar(x,am):
    v = {i:-1 for i in alp}
    nex = x
    count = 0
    fin = False
    while True:
        cur = nex
        if not fin:
            if v[cur] != -1:
                cyc = count-v[cur]
                am = count + (am-count)%cyc
                fin = True
                print(am)
            else:
                v[cur] = count
        count+=1
        nex = shuf[cur]
        if count == am: return nex
    

for x in alp:
    answers[x] = findchar(x,amount)
    


word = input()
ans = ''
for x in word:
    ans+=answers[x]
print(ans)
