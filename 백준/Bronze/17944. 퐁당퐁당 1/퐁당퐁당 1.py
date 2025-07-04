import sys
input = sys.stdin.readline

N,T = map(int,input().split())

res = (T-1)%(4*N-2)
if res > (2*N-1):
    print(4*N-1-res)
else:
    print(res+1)