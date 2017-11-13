'''
Explanation:
This works because 34! is a multiple of 2^32. You can see this by writing 34*33*...*2*1
and canceling out all factors of two out from all the numbers. You will see that this
ends up canceling exactly 32 twos and you are left with a bunch of odd numbers. Since 34! is
a multiple of 2^32 then n*34! is also a multple of 2^32 so every n! n>=34 % 2^32 = 0
'''
N = int(input())
for _ in range(N):
    n = int(input())
    if(n>33): print(0)
    else:
        mod = (1<<32)
        ans = 1
        for i in range(1,n+1):
            ans = ans*i%mod
        print(ans)
