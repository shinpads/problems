n = input().split()
city = ""
temp = 999999
while True:
    if int(n[1]) < temp:
        temp = int(n[1])
        city = n[0]
    if n[0] == "Waterloo":
        break
    n = input().split()
    
print(city)