import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
d = [(0,1), (1,0), (-1,0), (0,-1)]

N = int(input())
mirrors = []
door = []
board = []

for r in range(N):
    tmp = list(input().strip())
    for c in range(N):
        if tmp[c] == '!':
            mirrors.append((r,c))
        elif tmp[c] == '#':
            door.append((r,c))
    board.append(tmp)

n = len(mirrors) + 2
graph = [[] for _ in range(n+1)]
nodes = dict()
node = 2
nodes[door[0]] = 1
nodes[door[1]] = n
for mirror in mirrors:
    nodes[mirror] = node
    node += 1

#그래프 생성
def search(y,x):

        for i in range(4):
            for j in range(1,n):
                ny = y + d[i][0] * j
                nx = x + d[i][1] * j
                if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
                    break
                if board[ny][nx] == '*':
                    break
                if board[ny][nx] == '!' or board[ny][nx] == '#':
                    v1 = nodes[(y,x)]
                    v2 = nodes[(ny,nx)]
                    graph[v1].append(v2)
for i in range(2):
    search(door[i][0],door[i][1])
for i in range(n-2):
    search(mirrors[i][0],mirrors[i][1])

#다익스트라로 최단 거리 탐색
dist = [INF for _ in range(n+1)]
dist[1] = 0
hq = []
heapq.heappush(hq,(0,1))

while hq:
    cost,v1 = heapq.heappop(hq)
    if dist[v1] < cost:
        continue
    
    for v2 in graph[v1]:
        if cost + 1 < dist[v2]:
            dist[v2] = cost + 1
            heapq.heappush(hq,(cost+1,v2))
res = dist[-1]
if res == INF:
    print(0)
else:
    print(res-1)