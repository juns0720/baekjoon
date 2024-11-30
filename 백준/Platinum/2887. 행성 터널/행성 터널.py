import sys
input = sys.stdin.readline

n = int(input())
x,y,z = [],[],[]

for v in range(1,n+1):
    x1,y1,z1 = map(int,input().split())
    x.append([x1,v])
    y.append([y1,v])
    z.append([z1,v])
for pos in [x,y,z]:
    pos.sort()

res = 0
parent = [i for i in range(n+1)]
edges = []

for pos in [x,y,z]:
    for i in range(1,n):
        cv1,cv2 = pos[i-1][1], pos[i][1]
        cost = abs(pos[i][0] - pos[i-1][0])
        edges.append([cv1,cv2,cost])
edges.sort(key = lambda x: x[2])

def union(v1,v2):
    v1 = find_parent(v1)
    v2 = find_parent(v2)

    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

def find_parent(v1):
    if parent[v1] == v1:
        return v1
    parent[v1] = find_parent(parent[v1])
    return parent[v1]




for v1,v2,cost in edges:
    if find_parent(v1) != find_parent(v2):
        union(v1,v2)
        res+=cost

print(res)
