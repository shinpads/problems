#ECOO 2015 R1 P1
for i in range(10):
    n = input()
    time = 0
    colors = {"red":0,"blue":0,"green":0,"blue":0,"green":0,"yellow":0,"pink":0,"violet":0,"brown":0,"orange":0}
    while(n!= "end of box"):
        colors[n] +=1
        if n != "red":
            if (colors[n]-1) % 7 == 0 or colors[n] == 1:
                time +=13
        else:
            time +=16
        n = input()
        
    print(time)
