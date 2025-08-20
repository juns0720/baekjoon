import sys
input = sys.stdin.readline

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def isTrue(c1,c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2) <= (c1[2] + c2[2])**2

for tc in range(int(input())):

    n = int(input())
    circle = [list(map(int,input().split())) for _ in range(n)]
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if isTrue(circle[i],circle[j]):
                union(i,j)

    res = set()
    for i in range(n):
        res.add(find(i))
    print(len(res))