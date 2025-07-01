import sys
input = sys.stdin.readline
#상,하,좌,우
dy = [0,1,0,-1,0]
dx = [1,0,-1,0,0]
N = int(1e5)
INF = sys.maxsize

def cal_dist(y1,x1,y2,x2):
    return abs((y2-y1))+ abs((x2-x1))

n = int(input())
dp = [[INF for _ in range(5)] for _ in range(n+1)]
pos = [list(map(int,input().split())) for _ in range(n+1)]
for i in range(5):
    dp[0][i] = 0

#출발점 초기화
y1,x1 = pos[0][0], pos[0][1]
y2,x2 = pos[1][0], pos[1][1]

for i in range(5):
    ny2 = y2 + dy[i]
    nx2 = x2 + dx[i]

    if ny2 < 0 or ny2 > N-1 or nx2 < 0 or nx2 > N-1:
        continue
    dp[1][i] = cal_dist(y1,x1,ny2,nx2)

for i in range(2,n+1):
    y1,x1 = pos[i-1][0], pos[i-1][1]
    y2,x2 = pos[i][0], pos[i][1] 

    #도착 지점
    for j in range(5):
        ny2 = y2 + dy[j]
        nx2 = x2 + dx[j]

        if ny2 < 0 or ny2 > N-1 or nx2 < 0 or nx2 > N-1:
            continue
        #출발 지점
        for k in range(5):
            ny1 = y1 + dy[k]
            nx1 = x1 + dx[k]

            if ny1 < 0 or ny1 > N-1 or nx1 < 0 or nx1 > N-1:
                continue

            dp[i][j] = min(dp[i][j],dp[i-1][k] + cal_dist(ny1,nx1,ny2,nx2))

print(min(dp[-1]))
