import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int,input().split())) for _ in range(N)]

def cal_matrix(a,b):
    return a[0] * b[0] * b[1]

dp = [[sys.maxsize for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

#행렬의 길이
for i in range(1,N):
    # 시작점: j, 끝점: j+i, 간격: k
    for j in range(N):
        if j+i == N:
            break
        for k in range(j, j+i):
            dp[j][j+i] = min((\
                            dp[j][j+i],\
                            dp[j][k] + dp[k+1][j+i] + m[j][0] * m[k][1] * m[j+i][1],\
                             ))\

print(dp[0][N-1])