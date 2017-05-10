n = int(input())
for _ in range(n):
    l1,a1,l2,a2,lt,at = map(int,input().split())
    ans = "?"
    ammount = 1
    while l1*ammount < lt and a1*ammount < at:
        val1 = (at-(a1*ammount))/a2
        val2 = (lt-(l1*ammount))/l2
        if val1 == val2 and val1 > 0 and val1%1 == 0:
            if ans == "?":
                ans = str(ammount) + " " + str(int(val1))
            else:
                ans = "?"
                break
        ammount+=1
    print(ans)