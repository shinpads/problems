n = int(input())
for i in range(n):
    x = int(input())
    x = list(bin(x)[2:])
    for i in range(len(x)):
        if x[i] == "1":
            x[i] = "dank"
        else: x[i] = "meme"
    print(" ".join(x))