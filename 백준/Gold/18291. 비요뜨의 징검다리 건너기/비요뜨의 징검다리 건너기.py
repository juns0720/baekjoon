import sys
input = sys.stdin.readline

MOD = 10**9+7


for tc in range(int(input())):
    n = int(input())
    if n < 3:
        print(1)
    else:
        n-=2
        res = 1
        a = 2
        while n > 0:
            if n % 2 != 0:
                res = (res*a) % MOD
            n //= 2
            a = (a**2) % MOD
        print(res)