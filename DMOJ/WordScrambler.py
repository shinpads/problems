from itertools import permutations
n = list(input())
n.sort()
for x in permutations(n):
    print(''.join(x))