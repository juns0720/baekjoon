import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline

INF = sys.maxsize
dy = [-1,-1,1,1]
dx = [-1,1,-1,1]

n = int(input())
board = [[0 for _ in range(n)]for _ in range(n)]

region = []
cnt = 0
for i in range(n):
    tmp = list(map(int,input().split()))

    for j in range(len(tmp)):
        if tmp[j] == 2:
            sy,sx = i,j
        elif tmp[j] == 1:
            region.append((i,j))
            cnt += 1
        board[i][j] = tmp[j]

mo = (sy+sx) % 2


for y,x in region:
    if (y + x) % 2 != mo:
        print("Shorei")
        exit()

def cal_dist(y1,x1,y2,x2):
    x_gap = abs(x2-x1)
    y_gap = abs(y2-y1)

    return max(x_gap, y_gap)


min_dist = INF
visited = [0 for _ in range(len(region))]
def solve(y, x, dist, depth):
    global min_dist

    if depth == len(region):
        min_dist = min(min_dist, dist)
        return
    
    for i in range(len(region)):
        if visited[i]:
            continue

        ny,nx = region[i]

        visited[i] = 1
        solve(ny,nx,dist + cal_dist(y,x,ny,nx), depth + 1)
        visited[i] = 0

solve(sy,sx, 0, 0)

print("Undertaker")
print(min_dist)