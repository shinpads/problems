T = int(input())
def findDiv(x):
    xc = x.count("x")
    pc = x.count("^")
    if x.count("x") == 0: 
        return 0
    if x.count("^") == 0:        
        x = x.replace("x","")
        if x == " -":
            x = "-1" 
        if x == " ":
            x = "1"       
        return x
    p = int(x[x.index("^")+1:])
    a = x[:x.index("x")]
       
    if a == " ":
        a = 1
    elif a ==" -":
        a = -1
    elif a == " 0":
        return 0
    elif p == 0:
        return 0
    else:
        a = int(a)
    a *= p
    p -= 1
    
    if p == 1:
        x.replace("^","")
        p = ""
        if a == "-":
            a = -1
        if a == "1":
            a = ""
    elif p == 0:
        return a
    else:
        p = "^"+str(p)
    return str(a)+"x" + p
    
for i in range(T):
    y = input()[3:]
    print("y' =",findDiv(y))
    