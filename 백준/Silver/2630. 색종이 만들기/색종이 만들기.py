import sys
input = sys.stdin.readline
N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]
res = [0,0]

def cal(y1,y2,x1,x2):
    key = board[y1][x1]
    flag = True
    for y in range(y1,y2):
        if flag == True:
            for x in range(x1,x2):
                if board[y][x] != key:
                    flag = False
                    break
    if flag == False:
        my = (y1+y2)//2
        mx = (x1+x2)//2
        for i in range(2):
            if i == 0:
                (ty1,ty2) = (y1,my)
            else:
                (ty1,ty2) = (my,y2)
            for j in range(2):
                if j == 0:
                    (tx1,tx2) = (x1,mx)
                else:
                    (tx1,tx2) = (mx,x2)
                cal(ty1,ty2,tx1,tx2)

    else:
        res[key]+=1
cal(0,N,0,N)
for i in range(2):
    print(res[i])