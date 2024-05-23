import sys

input = sys.stdin.readline

MODULAR = 1000000007
M = int(input())

#분할정복 제곱 연산해서 계산
def recursion(x):
    if x == 1:
        return N
    v = recursion(x//2)
    if x%2 == 0:
        return v*v%MODULAR
    else:
        return v*v*N%MODULAR
#페르마의 소정리 다시 볼 것?

cnt = 0
for i in range(M):
    N,S = map(int,input().split())
    cnt = (cnt+recursion(MODULAR-2)*S%MODULAR)%MODULAR
print(cnt)