alp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ali = {alp[i]:i for i in range(26)}
w = input()
k = input()
k = k[:min(len(w),len(k))]
ans = ''

for i in range(len(k)):
    ans += alp[alp.index(w[i])-alp.index(k[i])%26]
for i in range(len(k),len(w)):
    # indi = indcypher - (indans(i-len(k))
    ans += alp[ali[w[i]] - ali[ans[i-len(k)]]%26]

print(ans)