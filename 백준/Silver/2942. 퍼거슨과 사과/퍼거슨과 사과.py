import sys
input = sys.stdin.readline


def gdc(a,b):
    while b > 0:
        a, b = b, a%b
    return a

R,G = map(int,input().split())

n = gdc(R,G)
for i in range(1, n+1):
    if R % i == 0 and G % i == 0:
        print(i,R//i,G//i)