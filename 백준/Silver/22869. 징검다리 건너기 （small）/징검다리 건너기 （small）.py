import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int,input().split()))
queue = deque([0])
visited = [0 for _ in range(n)]
def power(i,j):
    return (j-i) * (1+abs(a[i]-a[j]))
def bfs():
    while queue:
        i = queue.popleft()
        if i == n-1:
            print("YES")
            exit()
        for j in range(i+1,n):
            crnt_power = power(i,j)
            if not visited[j] and crnt_power <= k:
                queue.append(j)
                visited[j] = 1
    print("NO")

bfs()