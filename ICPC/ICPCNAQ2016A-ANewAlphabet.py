dic = {'a':'<tt>@</tt>','b':'8','c':'(','d':'|)','e':'3','f':'#','g':'6','h':'[-]','i':'|','j':'_|','k':'|<','l':'1','m':'[]\/[]','n':'[][]','o':'0','p':'|D','q':'(,)','r':'|Z','s':'$','t':'\'][\'','u':'|_|','v':'\/','w':'\/\/','x':'}{','y':'\'/','z':'2',}
word = ''
n = input()
for x in n:
    if x.lower() in dic.keys():
        word += dic[x.lower()]
    else:
        word+= x

print(word)