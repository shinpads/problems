n = int(input())
paths = dict()
cache = dict()
line= input().split()
line = [int(x) for x in line]

while line != [0,0]:
    if line[0] in paths.keys():
        paths[line[0]].append(line[1])
    else:
        paths[line[0]] = [line[1]]
    line= input().split()
    line = [int(x) for x in line]

def total(point):
    if point in cache.keys():
        return cache[point]
    if point == n:
        return 1
    else:
        if not point in paths.keys():
            return 0
        tot = sum([total(x) for x in paths[point]])
        cache[point] = tot
        return tot
print(total(1))