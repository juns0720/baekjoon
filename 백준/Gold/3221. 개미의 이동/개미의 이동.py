import sys
input = sys.stdin.readline

L, T = map(int,input().split())
N = int(input())
ants = [input().split() for _ in range(N)]

res = []
d = {'L': -1, 'D': 1}
for x, dir in ants:
    p = int(x) + d[dir] * T
    p %= (2 * L)
    if p < 0:
        p += 2 * L
    if p > L:
        p = 2 * L - p
    res.append(p)

print(*sorted(res))
