import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(n+3)]
dp[2] = 3
i = 4
if n % 2 == 1 or n == 0:
    print(0)
else:
    if n < 4:
        print(dp[n])
    else:
        while True:
            special = 0
            for j in range(1,(i-4)//2+1):
                special +=dp[2*j]

            dp[i] = dp[i-2]*3 + 2*(special) + 2
            if i == n:
                break
            i+=2
        print(dp[n])