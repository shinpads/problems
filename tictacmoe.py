board = []
for i in range(3):
    board.append(list(input()))
x = False
o = False
if ['X' for i in range(3)] in board:
    x = True
if ['O' for i in range(3)] in board:
    o = True
    
for i in range(3):
    if board[0][i] == board[1][i] == board[2][i]:
        if board[0][i] == 'X':
            x = True
        else:
            o = True
        
if board[0][0] == board[1][1] == board[2][2]:
    if board[0][0] == 'X':
        x = True
    else:
        o = True
if board[2][0] == board[1][1] == board[0][2]:
    if board[1][1] == 'X':
        x = True
    else:
        o = True
if x and not o:
    print("Timothy")
elif o and not x:
    print("Griffy")
elif not o and not x:
    print("Tie")
else:
    print("Error, redo")
            