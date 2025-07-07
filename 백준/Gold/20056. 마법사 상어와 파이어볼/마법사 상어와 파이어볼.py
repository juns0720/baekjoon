import sys
from copy import deepcopy
input = sys.stdin.readline

N,M,K = map(int,input().split())

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

fb = {}
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    #0: 질량, 1: 속력, 2:방향
    fb[(r-1,c-1)] = [[m,s,d]]

def convert_pos(y,x):

    if y < 0:
        ny = abs(y)
        if ny % N == 0:
            ny %= N
        else:
            ny = N-(ny%N)
    else:
        ny = abs(y)
        ny %= N
    if x < 0:
        nx = abs(x)
        if nx % N == 0:
            nx %= N
        else:
            nx = N-(nx%N)
    else:
        nx = abs(x)
        nx %= N
    return (ny,nx)

def create_fb(nfb,r,c,m,s,d):
    if (r,c) in nfb:
        nfb[(r,c)].append([m,s,d])
    else:
        nfb[(r,c)] = [[m,s,d]]

def move():
    global fb
    next_fb = {}
    #이동
    for r,c in deepcopy(list(fb.keys())):
        for i in range(len(fb[(r,c)])):
            m,s,d= fb[(r,c)][i][0], fb[(r,c)][i][1], fb[(r,c)][i][2]
            nr = r + dr[d]*s
            nc = c + dc[d]*s
            nr,nc = convert_pos(nr,nc)
            create_fb(next_fb,nr,nc,m,s,d)
    #검사
    divided_fb = {}
    for r,c in deepcopy(list(next_fb.keys())):
        total_fb = len(next_fb[(r,c)])
        if total_fb > 1:
            #파이어볼 나누기
            m = sum(next_fb[(r,c)][i][0] for i in range(total_fb)) // 5
            if m == 0:
                continue
            s = sum(next_fb[(r,c)][i][1] for i in range(total_fb)) // total_fb
            check = [0,0]
            for i in range(total_fb):
                if next_fb[(r,c)][i][2] % 2 == 0:
                    check[0] += 1
                else:
                    check[1] += 1
            if check[0] == 0 or check[1] == 0:
                for d in [0,2,4,6]:
                    create_fb(divided_fb,r,c,m,s,d)
            else:
                for d in [1,3,5,7]:
                    create_fb(divided_fb,r,c,m,s,d)
        else:
            create_fb(divided_fb,r,c,next_fb[(r,c)][0][0],next_fb[(r,c)][0][1],next_fb[(r,c)][0][2])
    fb = deepcopy(divided_fb)

for _ in range(K):
    move()

res = 0
for fireballs in fb.values():
    for fireball in fireballs:
        res += fireball[0]
print(res)