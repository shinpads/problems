paper = set(list(input()[1:]))

n = int(input())
for i in range(n):
    x = input()[1:]
    a = True
    for h in paper:
        if not h in x:
            a = False
            break
    if a: print('yes')
    else: print('no')