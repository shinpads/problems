import sys
input = sys.stdin.readline
amount = [0,0,1,1]

for i in range(123):
    amount.append(amount[-2] + amount[-3])

ranges = [(-1,-1),(-1,-1)]
for i in range(125):
    ranges.append((ranges[-1][1]+1,ranges[-1][1]+amount[i+2]))
   
def getlen(n):
    length = 2
    while n > ranges[length][1]:
        length+=1
    return length


def getseq(n):
    ans = ""
    length = getlen(n)    
    curIndex = n
    #print(ans,length,curIndex,ranges[length])
    while curIndex >= 0:
        if curIndex == 0:
            ans+= "69"
            break
        if curIndex == 1:
            ans+="420"
            break
        
        sixtynines = ranges[length][1] - amount[length-2] + 1# if you add a 69 to front
        fourtwenties = ranges[length][0] + amount[length-3] - 1
    
        if curIndex <= fourtwenties:
            ans += "420"
            length -= 3
            curIndex = (curIndex - ranges[length+3][0]) + ranges[length][0] 
        else:
            ans += "69"
            length -= 2
            curIndex = ranges[length][1] - (ranges[length+2][1] - curIndex)
        #print(ans,length,curIndex,ranges[length])
    print(ans)   


t = int(input())
for i in range(t):
    getseq(int(input())-1)