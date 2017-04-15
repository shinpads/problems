def main():
    for rob in range(10):
        n = int(input())
        t = input().split()
        t = [int(x) for x in t]
        total = 0
        for i in range(n-1,0,-1):
            x = t.index(i)        
            if not t[0] == i:
                if max(t[:x])>i:                
                    t.insert(0,t.pop(x))
                    total += x
        print(total)
main()