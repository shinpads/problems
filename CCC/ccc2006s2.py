plain = input()
ma = input()
message = input()
decrypt = {}
for i in range(len(ma)):
    decrypt[ma[i]] = plain[i]

ans = ""   
for x in message:
    if x in decrypt:
        ans += decrypt[x]
    else:
        ans += "."
print(ans)