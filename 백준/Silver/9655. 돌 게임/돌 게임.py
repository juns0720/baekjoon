import sys
input = sys.stdin.readline

def stone(i,n,Dp):
    if i > n:
        return
    if Dp[i-1] == 'SK':
        Dp[i] = 'CY'
        if n == i:
            return
        stone(i+1,n,Dp)

    elif Dp[i-1] == 'CY':
        Dp[i] = 'SK'
        if n == i:
            return
        stone(i+1,n,Dp)


n = int(input())

Dp = [0 for i in range(n+4)]
Dp[1],Dp[2],Dp[3] = 'SK','CY','SK'
i = 4
stone(i,n,Dp)
print(Dp[n])