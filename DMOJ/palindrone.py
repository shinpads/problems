
n = int(input())
if n == 1:
    print(9)
else:
    if n % 2 == 1:
        ni = round((((n-1)/2)-1))*"9"
        start = "10"
    else:
        ni = round((((n)/2)-1))*"9"
        start = "1"
    print(int(float("".join(start+ni+"8"))%1000000000))
    