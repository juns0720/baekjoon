import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())
derections = ((1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2))

for _ in range(test_case) :
  l = int(input())
  chess = [[0 for _ in range(l)] for _ in range(l)]
  visited = [[False for _ in range(l)] for _ in range(l)]

  start_x, start_y = map(int, input().split())
  visited[start_x][start_y] = True
  goal_x, goal_y = map(int, input().split())

  if start_x == goal_x and start_y == goal_y :
    print(0)
    continue

  q = deque()
  q.append((start_x, start_y))

  while len(q) :
    now_x, now_y = q.popleft()
    for d in derections :
      next_x = now_x + d[0]
      next_y = now_y + d[1]

      if next_x < 0 or next_y < 0 or next_x >= l or next_y >= l :
        continue
      if visited[next_x][next_y] :
        continue
      chess[next_x][next_y] = chess[now_x][now_y] + 1
      visited[next_x][next_y] = True
      q.append((next_x, next_y))
  print(chess[goal_x][goal_y])
      