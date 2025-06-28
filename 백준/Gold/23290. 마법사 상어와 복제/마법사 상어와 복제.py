import sys
from copy import deepcopy
input = sys.stdin.readline

def move_fish():
    update_fish_pos = {}
    for pos in list(fish_pos.items()):
        stay = [] # 이동 못하는 물고기
        fy = pos[0][0]
        fx = pos[0][1]
        for d in pos[1]: #해당 위치 물고기 이동
            move = 0 #이동 여부
            for i in range(d+8,d,-1):
                nd = i%8
                nfy = fy + fd[nd][0]
                nfx = fx + fd[nd][1]
                #범위 밖, 상어 칸, 냄새 칸이면 이동 불가
                if nfy < 0 or nfy > N-1 or nfx < 0 or nfx > N-1 or (nfy,nfx) == (sp[0],sp[1]) or board[nfy][nfx]:
                    continue
                if (nfy,nfx) in update_fish_pos:
                    update_fish_pos[(nfy,nfx)].append(nd)
                else:
                    update_fish_pos[(nfy,nfx)] = [nd]
                move = 1
                break
            if not move:
                stay.append(d)
        if stay:
            if (fy,fx) in update_fish_pos:
                update_fish_pos[(fy,fx)].extend(stay)
            else:
                update_fish_pos[(fy,fx)] = stay
    return update_fish_pos

def find_fish(sy,sx):
    if (sy,sx) in fish_pos:
        return len(fish_pos[(sy,sx)])
    else:
        return 0

def kill_fish(sy,sx):
    if (sy,sx) in fish_pos:
        fish_pos.pop((sy,sx))
        return 1
    else:
        return 0
def dfs(depth,path,fish,sy,sx):
    if depth < 0:
        shark_pos.append([path,fish])
        return

    for i in range(1,5):
        nsy = sy + sd[i][0]
        nsx = sx + sd[i][1]
        if nsy < 0 or nsy > N-1 or nsx < 0 or nsx > N-1:
            continue
        if visited[nsy][nsx]:
            crnt_fish = 0
        else:
            crnt_fish = find_fish(nsy,nsx)
        visited[nsy][nsx] += 1
        dfs(depth-1,path + i*(10**depth), fish+crnt_fish,nsy,nsx)
        visited[nsy][nsx] -= 1


def move_shark():

    fish = 0
    dfs(2,0,fish,sp[0],sp[1]) #최적의 상어 경로 찾기
    shark_pos.sort(key = lambda x : (-x[1],x[0]))

    paths = [int(i) for i in str(shark_pos[0][0])]
    for path in paths:
        sp[0] += sd[path][0]
        sp[1] += sd[path][1]
        if kill_fish(sp[0],sp[1]):
            board[sp[0]][sp[1]] = 2

def copy_fish():
    for pos in list(copy_fp.items()):
        fy,fx = pos[0][0],pos[0][1]
        for d in pos[1]:
            if (fy,fx) in fish_pos:
                fish_pos[(fy,fx)].append(d)
            else:
                fish_pos[(fy,fx)] = [d]



N = 4
fd = {0: (0,-1),1: (-1,-1),2: (-1,0),3: (-1,1),4: (0,1),5: (1,1),6: (1,0),7: (1,-1)}
sd = {1:(-1,0), 2:(0,-1), 3:(1,0), 4:(0,1)}
sp = [0,0]
fish_pos = {}
copy_fp = {}
board = [[0 for _ in range(4)] for _ in range(4)]

m,s = map(int,input().split())

for _ in range(m):
    fy,fx,d = map(int,input().split())
    fy-=1
    fx-=1
    d-=1
    if (fy,fx) in fish_pos:
        fish_pos[(fy,fx)].append(d)
    else: 
        fish_pos[(fy,fx)] = [d]

#상어 위치 갱신
sy,sx = map(int,input().split())
sp[0],sp[1] = sy-1,sx-1

#s회 반복
for _ in range(s):
    #물고기 이동
    copy_fp = deepcopy(fish_pos)
    fish_pos = move_fish()

    #상어 연속 3칸 이동
    shark_pos = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    #냄새 -1 
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                board[i][j]-=1
    move_shark()
    copy_fish()
res = 0
for i in list(fish_pos.items()):
    res += len(i[1])
print(res)