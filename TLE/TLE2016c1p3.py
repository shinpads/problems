n = input()
e = {'C':0,'H':0,'O':2}
r = {'C':1,'H':2,'O':3}
a,b = 0
for i in range(len(n)):
    
    if n[i] in ['C','H','O']:
        if i == len(n)-1:        
            e[n[i]] += 1
        elif n[i+1] in ['C','H','O']:
            e[n[i]] += 1
        else:
            e[n[i]] += int(n[i+1]) 
    
           
            
            
print(e)
        
        



