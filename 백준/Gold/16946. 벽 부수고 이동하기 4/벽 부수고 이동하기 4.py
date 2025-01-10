import sys
from collections import deque
input = sys.stdin.readline



def print_res():  
    for i in res:
        for j in i:
            print(j,end='')
        print()

N,M = map(int,input().split())
matrix = [list(map(int,str(input().strip()))) for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(team):
    cnt = 1
    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or ny > N-1 or nx < 0 or nx > M-1 or visited[ny][nx] or matrix[ny][nx] == 1:
                continue
            matrix[ny][nx] = team
            queue.append((ny,nx))
            visited[ny][nx] = 1
            cnt+=1

    return cnt

res = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

team = 2
dic = dict()
for row in range(N):
    for col in range(M):
        if matrix[row][col] == 0 and not visited[row][col]:
            queue = deque([(row,col)])
            visited[row][col] = 1
            matrix[row][col] = team
            cnt = bfs(team)
            dic[team] = cnt

            team+=1

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            res[y][x] = 1
            tmp = set()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if ny < 0 or ny > N-1 or nx < 0 or nx > M-1 or matrix[ny][nx] == 1:
                    continue
                tmp.add(matrix[ny][nx])
            for i in tmp:
                res[y][x] += dic[i]
            res[y][x] %= 10

print_res()