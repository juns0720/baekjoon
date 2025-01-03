import sys
input = sys.stdin.readline

N,R = map(int,input().split())

if N == 1:
    print(R*2)
else:
    print(N+1 + (R-1)*2)