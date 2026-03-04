import sys
import heapq
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]
R,C = 501,501
INF = sys.maxsize

board = [[0 for _ in range(R)] for _ in range(C)]

def init_board(r1,c1,r2,c2, value):
    for r in range(min(r1,r2), max(r1,r2)+1):
        for c in range(min(c1,c2), max(c1,c2)+1):
            board[r][c] = value

for i in range(int(input())):
    r1,c1,r2,c2 = map(int,input().split())
    init_board(r1,c1,r2,c2, 1)

for i in range(int(input())):
    r1,c1,r2,c2 = map(int,input().split())
    init_board(r1,c1,r2,c2, 2)

dist = [[INF for _ in range(R)] for _ in range(C)]
dist[0][0] = 0
hq = []

heapq.heappush(hq, (0,0,0))

while hq:
    cur_dist,y,x = heapq.heappop(hq)
    
    if dist[y][x] < cur_dist:
        continue
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny < 0 or ny > R-1 or nx < 0 or nx > C-1 or board[ny][nx] == 2:
            continue
            
        if cur_dist + board[ny][nx] < dist[ny][nx]:
            dist[ny][nx] = cur_dist + board[ny][nx]
            heapq.heappush(hq,(dist[ny][nx], ny, nx))

print(dist[R-1][C-1] if dist[R-1][C-1] != INF else -1)