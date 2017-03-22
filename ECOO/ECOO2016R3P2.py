for _ in range(10):
    aw, ah, sx, sy, vx, vy = map(int,input().split())
    ans = ""
    for i in range(5):
        th,tx,ty = map(int,input().split())
        if vx == 0 or sx > tx:
            ans+="M"
        else:            
            #t = d/v                 
            time = (tx-sx)/vx             
            vd = (vy*time) +sy 
            print(vd,ah)                
            vd = ah-(vd%ah)
                      
            if vd <= ty and vd >= (ty-th):
                
                ans += "H"
            else:
                ans += "M"
    print(ans)
