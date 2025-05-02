import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
enemies = [[] for _ in range(n+1)]
friends = [set() for _ in range(n+1)]
parent = [i for i in range(n+1)]

def union(v1,v2):
    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


for i in range(m):
    rel = input().strip().split()
    v1,v2 = int(rel[1]), int(rel[2])
    if rel[0] == "F":
        friends[v1].add(v2)
        friends[v2].add(v1)
    else:
        enemies[v1].append(v2)
        enemies[v2].append(v1)

for enemy in enemies:
    for i in range(len(enemy)):
        for j in range(len(enemy)):
            if i == j:
                continue
            friends[enemy[i]].add(enemy[j])
            friends[enemy[j]].add(enemy[i])
for v1 in range(1,n+1):
    for v2 in friends[v1]:
        if find(v1) != find(v2):
            union(v1,v2)

team = set()
for v in range(1,n+1):
    team.add(parent[v])
print(len(team))