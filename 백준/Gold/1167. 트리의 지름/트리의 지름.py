import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]


for _ in range(N):
    info = list(map(int,input().split()))[:-1]
    v1 = info[0]
    info = info[1:]
    for j in range(len(info)//2):
        graph[v1].append((info[j*2],info[j*2+1]))


def DFS(v1, cur_dist):
    for v2, dist in graph[v1]:
        if distance[v2] == -1:
            distance[v2] = cur_dist+dist
            DFS(v2,distance[v2])

distance = [-1 for _ in range(N+1)]
distance[1] = 0
DFS(1,0)

node = distance.index(max(distance))
distance = [-1 for _ in range(N+1)]
distance[node] = 0
DFS(node,0)

print(max(distance))