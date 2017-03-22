def main():
    s,k,i = map(int,input().split())
    lines = []
    lines.append([int(x) for x in input().split()])
    lines.append([int(x) for x in input().split()])
    lines.append([int(x) for x in input().split()])
    totalTime = 0
    def pass30(l):
        #print(l)
        if l == []:
            return([],0)
        l[0] -= 30
        while l[0] <= 0:
            if len(l) <= 1:
                return([],30+l[0])
            
            else:            
                ad = l.pop(0)
                l[0] += ad
        return (l,30)
    
    
    lengths = [s,k,i]
    maxTime = 0
    while lengths != [0,0,0]:                    
        maxTime = 0
        for i in range(3):
            lines[i], t = pass30(lines[i])
            #print(lines[i])
            if t > maxTime:
                maxTime = t
        totalTime += maxTime
        lengths = [len(x) for x in lines]         
        if lengths[0] != lengths[1] != lengths[2] != lengths[0]:            
            lines[lengths.index(max(lengths))].append(lines[lengths.index(min(lengths))].pop())
            
    print(totalTime)
    
main()