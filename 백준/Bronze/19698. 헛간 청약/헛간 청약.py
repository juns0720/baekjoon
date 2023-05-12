import sys
input = sys.stdin.readline

N,W,H,L = map(int,input().split())
res = (W//L) * (H//L)
if res >= N:
    print(N)
else:
    print(res)