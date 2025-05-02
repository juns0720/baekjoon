import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())
dist = [list(map(int,input().split())) for _ in range(n)]

def fw():
    for k in range(n):
        for s in range(n):
            for e in range(n):
                dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])

fw()
for i in range(m):
    a,b,c = map(int,input().split())
    if dist[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")