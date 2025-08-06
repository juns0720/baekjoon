import sys
from math import comb
input = sys.stdin.readline

for tc in range(int(input())):
    N,M,K,D = map(int,input().split())
    ac = comb(M,2)*N
    bc = M**2*comb(N,2)
    c = ac*K+bc
    value = D//c
    print(-1 if value == 0 else (ac*K+bc)*value)