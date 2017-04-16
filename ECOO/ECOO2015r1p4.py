for _ in range(10):
    n = input()
    p = set(["ook","ookook","oog","ooga","ug","mook","mookmook","oogam","oogum","ugug"])
    v = {}
    def find(x):    
        if x in v.keys():
            return v[x]        
        if x == "":
            return 1         
        tot = 0
        for i in range(2,len(x)+1):        
            if x[:i] in p:
                aa = x[i:]
                a = find(aa)
                v[aa] = a
                tot += a
        return tot    
    print(find(n))
