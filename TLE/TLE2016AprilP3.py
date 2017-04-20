n = int(input())


rows = [[]for i in range(10000)]
rows[2].append("69")
rows[3].append("420")

for i in range(2,49):
    rows[i].sort(key = lambda x: int(x))
    curr = rows[i]
    for x in curr:
        t = str(x+"69")

        rows[len(t)].append(t)
    for x in curr:
        t = str(x+"420")

        rows[len(t)].append(t)        


