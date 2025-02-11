import sys
input = sys.stdin.readline

INF = sys.maxsize
n = int(input())
W = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

def dfs(s, route):
    if dp[s][route] != -1:
        return dp[s][route]
    
    if route == (1 << n-1) -1:
        if not W[s][0]:
            return INF
        else:
            return W[s][0]
    
    min_dist = INF
    for e in range(1,n):
        #이동하지 못하거나 방문한 경우
        if not W[s][e] or route & (1 << e-1):
            continue
        
        dist = W[s][e] + dfs(e, route | (1 << e-1))
        if min_dist > dist:
            min_dist = dist
    dp[s][route] = min_dist
    return min_dist

res = dfs(0,0)
print(res)