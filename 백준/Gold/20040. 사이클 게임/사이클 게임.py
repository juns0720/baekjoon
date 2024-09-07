import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N)]


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1,v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1

cnt = 0
for _ in range(M):
    v1,v2 = map(int,input().split())
    cnt+=1
    if find(v1) != find(v2):
        union(v1,v2)
    else:
        print(cnt)
        exit()
print(0)