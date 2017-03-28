def main():
    def encode(x):   
        y = x.split()
        y = [list(t) for t in y]
        a = ""
        while len(max(y)) > 0:              
            for i in range(len(y)):
                if len(y[i]) > 0:
                    a += y[i].pop(0)
        answer = []
        index = 0
        for z in x.split():
            answer.append(a[index:index+len(z)])
            index += len(z)
        return " ".join(answer)
    
    def secondmax(x):
        x=set(x)    
        x.remove(max(x))
        if len(x) > 0:
            return max(x)
        else: return 0
    def decode(x):
        lens = [len(i) for i in x.split()]
        a = ["" for i in range(len(x.split()))]
        x = list(x.replace(" ", ""))    
        while len(x) > 0:                
            maxX = max(lens)
            secX = secondmax(lens)        
            c = maxX - secX
            nums = []        
            for k in range (len(lens)):
                if lens[k] == maxX:
                    nums.append(k)
                    
            lens = [k if k != maxX else secX for k in lens]  
            nums.reverse()                   
            for i in range(c):                     
                for y in nums:
                    a[y] = x.pop() + a[y]
        return  " ".join(a)
    for _ in range(10):
        n = input()
        a = input()
        if n == "decode":
            print(decode(a))
        else:print(encode(a))
main()