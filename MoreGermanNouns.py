

n = int(input())
for i in range(n):
    line = input().split()
    line[-1] = list(line[-1])
    line[-1][-1] = ""
    line [-1] = "".join(line[-1])
    for x in line:
        if x[0] == x[0].upper():            
            print(str(str.encode(x),"utf-8"))

