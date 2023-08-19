import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
graph = [abs(K-N) for _ in range((K+N)*2+1)]
visited = [0 for _ in range((K+N)*2+1)]
graph[N] = 0
visited[N] = 1
queue = deque([N])
def BFS():
    while queue:
        n = queue.popleft()
        dn = [-1,1,n]
        for i in range(3):
            tn = n+dn[i]
            if tn > -1 and tn < K*2+1 and not visited[tn]:
                queue.append(tn)
                visited[tn] = 1
                graph[tn] = graph[n]+1
    print(graph[K])
BFS() 