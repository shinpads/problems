n = int(input())
start = [input() for i in range(n)]

def remove(l):
    l = "".join(l)
    l = l.replace('1111111','0000000')
    l = l.replace('111111','000000')
    l = l.replace('11111','00000')
    l = l.replace('1111','0000')
    return list(l)
def getcount(l):    
    return l.count('1')

q = [(start,0)]
v = [False for i in range(n+1)]
v[getcount(start)] = True
found = False
while len(q) > 0:
    cur,moves = q.pop(0)
    print(cur,moves)
    for i in range(len(cur)):
        if cur[i] == '0':
            cop = list(cur)
            cop[i] = '1'
            cop = remove(cop)
            val = getcount(cop)
            if val == 0: print(moves+1);found = True;break
            if not v[val]:

                q.append((cop,moves+1))
                v[val] = True
    if found: break
print(v)     
