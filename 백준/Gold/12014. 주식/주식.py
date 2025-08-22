import sys
input = sys.stdin.readline

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    res = 1
    dp = [1 for _ in range(N)]

    for i in range(1,N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+1, dp[i])

    if max(dp) < K:
        res = 0
    print(f"Case #{tc}")
    print(res)
