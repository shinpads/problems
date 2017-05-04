for _ in range(10):
    alp = "abcdefghijklmnopqrstuvwxyz"
    alpind = {}
    for i in range(len(alp)):
        alpind[alp[i]] = i
        
    
    def encode(n,w):
        w = w.split()
        ans = []
        for x in range(len(w)):
            word = ""
            for y in range(len(w[x])):
                word += alp[(alpind[w[x][y]]+n)%26]
            ans.append(word)
        t = alp[n]
        if n < 0: t = ""
        return t + " ".join(ans)           
    
    
    ed = input()
    if ed == "encode":
        n = int(input())
        w = input()   
        print(encode(n,w))
    else:
        w = input()
        v = w[0]
        w = w[1:]
        v = alpind[v]
        print(encode(-v,w))
    