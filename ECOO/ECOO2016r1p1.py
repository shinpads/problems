passe = []
for ge in range(10):
    wts = input().split()
    wts = [int(x)*0.01 for x in wts]
    wT = wts[0]
    wA = wts[1]
    wP = wts[2]
    wQ = wts[3]
    
    n = int(input())
    passes = 0
    for i in range(n):
        m = input().split()
        m = [int(x) for x in m]
        if (m[0] * wT) + (m[1] * wA)+(m[2] * wP)+(m[3] * wQ) >= 50:
            passes +=1
            
    passe.append(passes)
a = ""
for i in passe:
    print(i)

    

    
    
    
    
    
    
    