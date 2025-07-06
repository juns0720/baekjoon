from copy import deepcopy
import sys
input = sys.stdin.readline

#상하좌우
dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]


shark = dict()
cnt = 0
N,M,K = map(int,input().split())
total_shark = M
smell = {}
for y in range(N):
    tmp = list(map(int,input().split()))
    for x in range(N):
        if tmp[x]:
            shark[tmp[x]] = (y,x)
            smell[(y,x)] = [tmp[x],K]
crnt_d = [0] + list(map(int,input().split()))

sd = [[] for _ in range(M+1)]
for i in range(1,M+1):
    sd[i] = [0] + [list(map(int,input().split())) for _ in range(4)]

def move():
    global total_shark
    #1번 상어부터 순차적으로 이동
    next_shark = dict()
    for i in range(1,M+1):
        if crnt_d[i] == -1:
            continue
        cd = crnt_d[i]
        y,x = shark[i]
        path = [[],[]]
        for j in sd[i][cd]:
            ny = y + dy[j]
            nx = x + dx[j]
            if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
                continue
            if (ny,nx) in smell:
                #나의 냄새가 아니라면
                if smell[(ny,nx)][0] != i:
                    continue
                else:
                    path[1].append((ny,nx,j))
            else:
                path[0].append((ny,nx,j))
        if path[0]:
            py,px,dir = path[0][0][0],path[0][0][1],path[0][0][2]
        else:
            py,px,dir = path[1][0][0],path[1][0][1],path[1][0][2]

        if (py,px) in next_shark:
            next_shark[(py,px)].append([i,dir])
        else:
            next_shark[(py,px)] = [[i,dir]]

    for i in next_shark.keys():
        if len(next_shark[i]) > 1:
            for j in range(1,len(next_shark[i])):
                ns,ndir = next_shark[i][j]
                crnt_d[ns] = -1
                total_shark-=1
                shark.pop(ns)
        crnt_d[next_shark[i][0][0]] = next_shark[i][0][1]
        shark[next_shark[i][0][0]] = i
    #냄새 없애기
    smell_keys = deepcopy(list(smell.keys()))
    for k in smell_keys:
        smell[k][1] -= 1
        if smell[k][1] == 0:
            smell.pop(k)
    #냄새 뿌리기
    for i in range(1,M+1):
        if crnt_d[i] == -1:
            continue
        y,x = shark[i]
        smell[(y,x)] = [i,K]


for s in range(1,1001):
    move()
    if total_shark == 1 and crnt_d[1] != -1:
        print(s)
        exit()
print(-1)       