import sys

input = sys.stdin.readline
d = int(input())
clubs = []
for _ in range(int(input())):
    clubs.append(int(input()))
clubs.sort()
clubs.reverse()
cm = 999999999
v = set([])
def tryClub(cd,ns): #curDis, numStrokes 
    global cm   
    if ns >= cm:
        return 999999999
    if cd == 0:
        if ns < cm:
            cm = ns
        return ns
    if cd < 0:
        return 999999999
    if cd in v:
        return 999999999
    else:
        v.add(cd)
    return min([tryClub(cd-x,ns+1) for x in clubs])

a = tryClub(d,0)
if a == 999999999:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in " + str(a) +" strokes.")
           