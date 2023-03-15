import sys
input = sys.stdin.readline

def P(n,dp,i):
    if n <= 2:
        return
    else:
        if dp [i] != 0:
            if n == i:
                return
            P(n,dp,i+1)

        else:   
            dp[i] = dp[i-3]+dp[i-2]
            if n == i:
                return
            P(n,dp,i+1)

        
    
n = int(input())
Dp = [0 for i in range(101)]
Dp[0],Dp[1],Dp[2] = 1,1,1   #Dp[i] = Dp[i-3]+Dp[i-2]
cnt = 3
for i in range(n):
    t = int(input())
    P(t,Dp,cnt)
    print(Dp[t-1])
