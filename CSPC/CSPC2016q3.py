import sys
input = sys.stdin.readline
def correct(x):
    x = list(x)
    i = 0
    while i < len(x):        
        if x[i] == "c":
            if i < len(x)-2:
                if x[i+1]+x[i+2] == "ie":                    
                    x[i+1] = "e"
                    x[i+2] = "i"
                    i+= 3
                    continue
                elif x[i+1]+x[i+2] == "ei":                    
                    i+=3
                    continue
                    
        if x[i] == "e":
            if x[i+1] == "i":
                x[i] = "i"
                x[i+1] = "e"
        i+=1
    return "".join(x)
wn = 1 

             
while True:
    n = input()    
    if n.split() == "No More Words!".split():        
        break
    else:
        a = correct(n)
        if n == a:
            print("Word",wn,"is correct.")
        else:
            print(a)
        wn+=1