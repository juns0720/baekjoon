import sys
input = sys.stdin.readline

MOD = 1000000009
N = int(input())
if N == 1:
    print(0)
    exit()
print(2*3**(N-2)%MOD)