import sys
input = sys.stdin.readline

N = int(input())

std = [list(input().strip()) for _ in range(N)]

n = len(std[0])

for i in range(n-1,-1,-1):
    res = set()
    for j in range(N):
        res.add(''.join(std[j][i:]))
    if len(res) == N:
        print(n-i)
        exit()