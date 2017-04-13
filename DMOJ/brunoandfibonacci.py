n = int(input())
fib = [False for i in range(n+1)]
fib[1] = True
a = 2; b = 1; c = 1;
while a < n:
    fib[a] = True
    c = b
    b = a
    a = b+c

def dostuff():
    s = input()
    for i in range(n):
        if s[i] == "A":
            if not fib[i+1]:
                return False  
        else:
             if fib[i+1]: return False
    return True

if dostuff():
    print("That's quite the observation!")
else:
    print("Bruno, GO TO SLEEP")