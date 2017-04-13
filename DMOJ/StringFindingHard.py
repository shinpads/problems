
s = input()
t = input()
lt = len(t)
#Bad Match Table
v = {}
for i in range(lt-1):
    v[t[i]] = lt - i - 1
v[t[-1]] = lt-1
#print(v)
ff = True
d = False
for a in range(len(s)-len(t)+1):
    if s[a] == t[0]:
        for b in range(a+len(t)-1,a,-1):
            ff = True
            if s[b] != t[b-a]:
                ff = False
                if s[b] in v.keys():
                    a+= v[s[b]]
                else: a+= lt-1
                    
                break
        if ff:
            d = True
            print(a)
            break
if d == False:
    print(-1)