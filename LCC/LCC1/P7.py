for _ in range(10):
    n = int(input())
    vals = {}
    for i in range(n):
        item,price = input().split(); price = int(price)
        if item in vals.keys():
            vals[item] = min(vals[item],price)
        else:
            vals[item] = price
            
    m = int(input())
    total = 0
    for i in range(m):
        item = input()
        total+=vals[item]
    print(total)