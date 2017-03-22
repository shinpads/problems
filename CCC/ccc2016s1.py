n = input()
a = input()
s1 = n.count("*")
n.replace("*","")
s2 = a.count("*")
a.replace("*","")
p = set(n)
f= 0
for x in p:
    f += abs(n.count(x) - a.count(x))
       
if f == abs(s1-s2):
    print("A")
else:
    print("N")
