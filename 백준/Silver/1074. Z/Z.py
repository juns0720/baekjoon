import sys
input = sys.stdin.readline

N,Y,X = map(int,input().split())

n_pos = [0,0]

def Z(y,x,res,n):
    flag = False
    if n_pos[0] == Y and n_pos[1] == X:
        return res
    if n == 1:
        for ty in range(y,y+2):
            for tx in range(x,x+2):
                res+=1
                if ty == Y and tx == X:
                    n_pos[0] = ty
                    n_pos[1] = tx
                    return res
    else:
        m = (2**n)//2
        for ty in range(y,y+m+1,m):
            if flag == True:
                break
            for tx in range(x,x+m+1,m):
                if Y < ty+m and Y > ty-1 and X < tx+m and X > tx-1:
                    res = Z(ty,tx,res,n-1)
                    flag = True
                    break
                else:
                    res+=(m*m)
    return res
if Y == 0 and X == 0:
    print(0)
else:
    print(Z(0,0,-1,N))
