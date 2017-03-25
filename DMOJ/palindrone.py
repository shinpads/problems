
n = int(input())
if n == 1:
    print(9)
else:
    if n % 2 == 1:
        ni = int((((n-1)/2)-1))*"9"
        start = "10"
    else:
        ni = int((((n)/2)-1))*"9"
        start = "1"
    print(int(float(start+ni+"8")%1000000000))
    