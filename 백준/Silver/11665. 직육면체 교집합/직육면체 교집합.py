import sys
input = sys.stdin.readline

N = int(input())
x = [1, 1000]
y = [1, 1000]
z = [1, 1000]

for _ in range(N):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())

    xa, xb = sorted([x1, x2])
    ya, yb = sorted([y1, y2])
    za, zb = sorted([z1, z2])

    x[0] = max(x[0], xa)
    x[1] = min(x[1], xb)
    y[0] = max(y[0], ya)
    y[1] = min(y[1], yb)
    z[0] = max(z[0], za)
    z[1] = min(z[1], zb)

vol = max(0, x[1] - x[0]) * max(0, y[1] - y[0]) * max(0, z[1] - z[0])
print(vol)
