#ECOO 2013 R1 P2
from math import ceil
def main():
    def getSum(x):
        x = [int(b) for b in x]
        for i in range(len(x)-1,-1,-2):                
            x[i] = list(str(2*x[i]))        
            if len(x[i]) > 1:
                x[i] = int(x[i][0])+int(x[i][1])
            else:
                x[i] = int(x[i][0])
        return sum(x)
    answers = []
    for i in range(5):
        answer = ""
        nums = input().split()
        nums = [list(x) for x in nums]
        for a in nums:
            y = getSum(a)    
            answer += str(abs(10*ceil(0.1*y)-y))        
        answers.append(answer)
        
    for x in answers:
        print(x)
main()
