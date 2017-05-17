r = int(input())
l = int(input())
def xor(a,ind):
    res = ""
    for i in range(len(a)):
        if a[i] == lights[ind][i]:
            res+= '0'
        else:
            res += '1'
    return res
        
lights = ["".join(input().split()) for i in range(r)]

lastrow = set()
lastrow.add(lights[0])
for i in range(1,r):
    nextrow = set()
    for x in lastrow:
        nextrow.add(xor(x,i))


    nextrow.add(lights[i])

    lastrow = nextrow
print(len(lastrow))

