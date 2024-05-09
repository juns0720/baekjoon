import sys
input = sys.stdin.readline

N = int(input())
al = list(map(int,input().split()))

forward_dp = [1 for i in range(N+1)]
reverse_dp = [0 for i in range(N+1)]

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if al[j-1] > al[i-1]:
            forward_dp[j] = max(forward_dp[j], forward_dp[i]+1)

for i in range(N,0,-1):
    for j in range(i-1,0,-1):
        if al[j-1] > al[i-1]:
            reverse_dp[j] = max(reverse_dp[j] , reverse_dp[i]+1)

# print(forward_dp)
# print(reverse_dp)

res = 0
for i in range(1,N+1):
    res = max(res, forward_dp[i] + reverse_dp[i])
print(res)
