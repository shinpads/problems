x = input()
a = x.count(':-)')
s = x.count(':-(')
if a>s:
    print("happy")
elif a == s == 0:
    print("none")
elif a == s:
    print("unsure")
else:
    print("sad")