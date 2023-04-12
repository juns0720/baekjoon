import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    if N % H == 0:
        b = N//H
        res = H*100+b
    else:
        a = N%H
        b = N//H
        res = a*100+b+1
    print(res)
