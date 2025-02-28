import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
before = [list(map(int,input().split())) for _ in range(n)]
after =[list(map(int,input().split())) for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(key,key2):
  cnt = 0
  while queue:    
    y,x = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny > n-1 or nx < 0 or nx > m-1 or visited[ny][nx] or before[ny][nx] != key:
          continue
      before[ny][nx] = key2
      visited[ny][nx] = 1
      queue.append((ny,nx))
      cnt+=1
  return cnt



visited = [[0 for _ in range(m)] for _ in range(n)]


for r in range(n):
  for c in range(m):
    if not visited[r][c] and before[r][c] != after[r][c]:
      queue = deque([(r,c)])
      visited[r][c] = 1
      bfs(before[r][c], after[r][c])
      before[r][c] = after[r][c]

      for r in range(n):
        for c in range(m):
          if before[r][c] != after[r][c]:
            print("NO")
            exit()
      print("YES")
      exit()
print("YES")