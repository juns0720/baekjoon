import sys
input = sys.stdin.readline

def Tile(i,Dp,n):
    if i > n:
        return
    if i > 2:
        Dp[i] = Dp[i-1]+Dp[i-2]
        if i == n:
            return Dp[i]
        else:
            Tile(i+1,Dp,n)



n = int(input())
Dp = [0 for i in range(n+3)]
cnt = n
Dp[1] = 1
Dp[2] = 2
Dp[3] = 3
i = 3
Tile(i,Dp,n)
print(Dp[n]%10007)

