import sys
import heapq
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]
INF = sys.maxsize
N,M = map(int,input().split())

Tg,Tb,X,B = map(int,input().split())


hq = []
visited = [[INF for _ in range(M)] for _ in range(N)]
board = []
for i in range(N):
    tmp = list(input().strip())
    for j in range(M):
        if tmp[j] == '*':
            visited[i][j] = 0
            heapq.heappush(hq,(0,i,j))
    board.append(tmp)


def dijkstra():
    while hq:
        cost, y,x = heapq.heappop(hq)

        if visited[y][x] < cost:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny > N-1 or nx < 0 or nx > M-1 or visited[ny][nx] <= visited[y][x] + 1:
                continue

            if board[ny][nx] == '#':

                if visited[ny][nx] <= visited[y][x] + 1 + Tb:
                    continue
                visited[ny][nx] = visited[y][x] + 1 + Tb

            else:
                visited[ny][nx] = visited[y][x] + 1
            heapq.heappush(hq,(visited[ny][nx],ny,nx))
dijkstra()

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] > Tg:
            cnt += 1
            print(i+1,j+1)
if not cnt:
    print(-1)