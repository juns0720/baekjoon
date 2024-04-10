import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int,input().split())
matrix = [list(map(int,input().strip())) for _ in range(row)]
queue = deque([])
visited = [[[0,0] for _ in range(col)] for _ in range(row)]


def BFS():
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    queue.append((0,0,0))
    visited[0][0][0] = 1

    while queue:
        y, x, w = queue.popleft()
        if (y == row-1 and x == col-1):
            return visited[y][x][w]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ((ny > -1 and ny < row and nx > -1 and nx < col) and not visited[ny][nx][w]):
                if (matrix[ny][nx] == 1 and w == 0):
                    visited[ny][nx][w+1] = visited[y][x][w] + 1
                    queue.append((ny,nx,w+1))
                elif(matrix[ny][nx] == 0):
                    visited[ny][nx][w] = visited[y][x][w] + 1
                    queue.append((ny,nx,w))
    return -1


print(BFS())
