import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())

rain = []
for i in range(m):
    rain.append(list(map(int,input().split())))

cost, floor = 0,INF
for i in range(m):
    t,r = rain[i]
    if t <= floor:
        cost += r
        floor = t
    else:
        cost += r
    if cost > k:
        print(i+1, floor)
        exit()
print(-1)