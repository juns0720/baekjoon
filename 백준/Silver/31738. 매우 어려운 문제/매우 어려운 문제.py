import sys
input = sys.stdin.readline

n,m = map(int,input().split())

if n >= m:
    print(0)
else:
    res = 1
    for i in range(1,n+1):
        res*=(i%m)
        res%=m
    print(res)
    