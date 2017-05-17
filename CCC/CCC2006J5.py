"""
M-Word = A-word, 'N', A-Word
A-Word = 'A' or 'B', M-Word, 'S'
"""
word = input()

def aword(word):
    if word == "":
        return 0
    if word[0] == "A" and len(word) == 1:
        return 1
    elif word[0] == "B" and len(word)>1:
        if mlang(word[1:-1]) and word[-1] == 'S':
            return 1
    else:
        return 0
    
def mlang(word):
    if aword(word):
        return 1
    size = 0
    for i in range(len(word),-1,-1):        
        if aword(word[0:i]):
            size = i
            break
    
    if len(word) > size+1:
        if word[size] == 'N' and mlang(word[size+1:]):
            return 1
    return 0
    
while word != "X":
    if mlang(word):
        print("YES")
    else:
        print("NO")
    word = input()