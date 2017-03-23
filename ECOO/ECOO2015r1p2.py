for _ in range(10):
    W = int(input())
    n = input().split()
    n.append("")
    cl = 0
    line = []
    for x in n:        
        while cl-1 > W:        
            print(line[0][:W])
            line = [line[0][W:]]            
            cl = len(line[0])+1
        if cl+len(x) <= W:
            line.append(x)
            cl+=len(x)+1
        else:
            print(" ".join(line))
            cl = len(x) + 1
            line = [x]
    if len(" ".join(line)) > 0 :        
        print(" ".join(line))
    print("=====")