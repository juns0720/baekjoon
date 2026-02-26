import sys
input = sys.stdin.readline

INF = sys.maxsize
while True:
    try:
        n, s, t = map(int,input().split())
    except:
        break
    costs = []
    cnt = 0
    while cnt < n:

        tmp = list(map(int,input().split()))
        cnt += len(tmp)
        costs.extend(tmp)


    dp = [[-INF for _ in range(n)] for _ in range(t-1)]
    for i in range(s):
        dp[0][i] = costs[i]
    answer = -INF
    for i in range(1,t-1):    # 현재 턴
        for j in range(n):      # 현재 위치
            for k in range(1,s+1):  # 이동 범위
                if j+k > n-1:
                    break

                dp[i][j+k] = max(dp[i][j+k], dp[i-1][j]+costs[j+k])
                if i < t:
                    for z in range(n-1,n-1-s,-1):
                        answer = max(answer, dp[i][z])

    print(answer)