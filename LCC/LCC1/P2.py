for _ in range(10):
    b = int(input())
    n = int(input())
    for i in range(n):
        x = int(input())
        if x > b: print("world record"); b=x
        else: print("nice try")
