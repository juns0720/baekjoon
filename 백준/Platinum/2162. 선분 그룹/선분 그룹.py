import sys
input = sys.stdin.readline


def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

def check(p1,p2):
    ccw123 = ccw(p1[0],p1[1],p1[2],p1[3],p2[0],p2[1])
    ccw124 = ccw(p1[0],p1[1],p1[2],p1[3],p2[2],p2[3])
    ccw341 = ccw(p2[0],p2[1],p2[2],p2[3],p1[0],p1[1])
    ccw342 = ccw(p2[0],p2[1],p2[2],p2[3],p1[2],p1[3])
    l12 = ccw123 * ccw124
    l34 = ccw341 * ccw342
    if l12 == 0 and l34 == 0:
        if min(p1[0],p1[2]) <= max(p2[0],p2[2]) and min(p2[0],p2[2]) <= max(p1[0],p1[2]) and \
           min(p1[1],p1[3]) <= max(p2[1],p2[3]) and min(p2[1],p2[3]) <= max(p1[1],p1[3]):
            return 1
        
    elif l12 < 1 and  l34 < 1:
        return 1

    return 0

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    v1, v2 = find(x), find(y)

    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

n = int(input())
pos = [list(map(int,input().split())) for _ in range(n)]

parent = [i for i in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if check(pos[i], pos[j]):
            union(i,j)

cnt = 0
lines = [0 for _ in range(n)]

for i in range(n):
    if i == parent[i]:
        cnt += 1
    lines[find(i)] += 1
print(cnt)
print(max(lines))
