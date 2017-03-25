gamesLeft = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

points = [0 for i in range(5)]
T = int(input())
G = int(input())
games = []
for i in range(G):
    game = input().split()
    game = [int(k) for k in game]
    gamesLeft.remove([game[0],game[1]])
    if game[2] > game[3]:
        points[game[0]] += 3
    elif game[3] > game[2]:
        points[game[1]] +=3
    else:
        points[game[0]] +=1
        points[game[1]] +=1
        
    games.append(game)



def wins(gamesLeft,pts,game,win):
    
    if win == 1:
        pts[game[0]] +=3
    elif win == 0:
        pts[game[0]] +=1
        pts[game[1]] +=1
    elif win == -1:
        pts[game[1]] +=3    
    if gamesLeft == []:        
        for i in range(1,5):
            if not i == T:
                if not pts[T] > pts[i]:
                    return 0
        return 1
    else:       
        nextGame = gamesLeft.pop()
        return sum([wins(list(gamesLeft),list(pts),nextGame,k) for k in range(-1,2)])

print(wins(list(gamesLeft),points,[0,0],2))