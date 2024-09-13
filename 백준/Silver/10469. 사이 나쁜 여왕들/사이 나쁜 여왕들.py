import sys
from collections import deque
input = sys.stdin.readline


board = [list(input().strip()) for _ in range(8)]

# 증가하는 방향
dy = [0,1,1,1]
dx = [1,0,1,-1]
cnt = 0
def check(row,col):

   for d in range(4):
      queue = deque()
      queue.append((row,col))
      while True:
         y,x = queue.popleft()
         
         ny = y+dy[d]
         nx = x+dx[d]
         if ny < 0 or ny > 7 or nx < 0 or nx > 7:
            break
         if board[ny][nx] == '*':
            print("invalid")
            exit()

         queue.append((ny,nx))



for row in range(8):
   for col in range(8):
      if board[row][col] == '*':
         check(row,col)
         cnt+=1

print("valid") if cnt == 8 else print("invalid")