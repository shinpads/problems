#ECOO 2013 R1 P1
start=int(input())
numOfStudents=0
served = 0

input1=input()

while(input1!="EOF"):
    if(start>999):
        start=1
    
    if(input1 == "TAKE"):
        numOfStudents+=1
        start+=1
    
    if(input1 == "SERVE"):
        served+=1
        
    if(input1 == "CLOSE"):
        print(str(numOfStudents)+" "+str(numOfStudents-served)+" "+str(start))
        numOfStudents=0
        served=0
        
    input1=input()
