import sys
input = sys.stdin.readline

N = int(input())
MAX_SIZE = int(1e6)+1

x = [0 for _ in range(MAX_SIZE)]
y = [0 for _ in range(MAX_SIZE)]

for i in range(N):
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    sx,ex = min(x1,x2,x3), max(x1,x2,x3)
    sy,ey = min(y1,y2,y3), max(y1,y2,y3)

    if ex-sx > 1:
        x[sx+1] += 1
        x[ex] -= 1
    
    if ey-sy > 1:
        y[sy+1] += 1
        y[ey] -= 1

for i in range(1, MAX_SIZE):
    x[i] = x[i-1]+x[i]
    y[i] = y[i-1]+y[i]

M = int(input())

for i in range(M):
    q = input().strip().split(' ')
    num = int(q[2])
    
    if q[0] == 'x':
        print(x[num])
    elif q[0] == 'y':
        print(y[num])