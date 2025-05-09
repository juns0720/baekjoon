import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))


INF = sys.maxsize
def cal(i,j):
    return (j-i)*(1+abs(A[i]-A[j]))

max_power = 0
dp =[INF for _ in range(n)]
dp[0] = 0

for i in range(n):
    for j in range(i+1,n):
        power = cal(i,j)
        dp[j] = min(dp[j], max(dp[i],power))
print(dp[n-1])
