n = int(input())
n = n%1000000000
if n == 1:
    print(9)
else:
    if n % 2 == 1:
        ni = int((((n-1)/2)-1))*"9"
        start = "10"
    else:
        try:
            ni = int((((n)/2)-1))*"9"
            start = "1"
        except: pass
    try:
        print(int("".join(start+ni+"8"))%1000000000)
    except: pass