units = input().split()
units = [int(x) for x in units]
people = input().split()
people = [int(x) for x in people]
total = 0

c = {}
c[0] = (0,)
c[1] = (0,1)
c[2] = (0,2)
c[3] = (0,1,2,3)
c[4] = (0,4)
c[5] = (0,1,4,5)
c[6] = (0,2,4,6)
c[7] = (0,1,2,3,4,5,6,7)

finished = []
num = -1
while len(finished) != 8:
    for i in range(8):
        if not i in finished:
            bloodTypes = c[i]            
            bloodType = bloodTypes[num]
            withdraw = min(units[bloodType],people[i])
            units[bloodType] -= withdraw
            people[i] -= withdraw
            total += withdraw
            if abs(num) == len(bloodTypes):
                finished.append(i)        
    num -=1
print(total)