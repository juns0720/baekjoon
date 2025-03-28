import sys
from collections import deque
input = sys.stdin.readline

d = [
    [1,2,4],[1,2,3,5],[2,3,6],
    [1,4,5,7],[2,4,5,6,8],[3,5,6,9],
    [4,7,8],[5,7,8,9],[6,8,9]
    ]


def conversion(board):
    tmp = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                tmp |= (1 << (i*3 + j + 1))

    return tmp


def bfs():

    while queue:
        board, cnt = queue.popleft()
        if board == 0:
            return cnt
        for i in range(9):
            tmp = board
            for j in d[i]:
                tmp ^= (1 << j)
            if visited[tmp]:
                continue
            queue.append((tmp, cnt + 1))
            visited[tmp] = 1

for tc in range(int(input())):
    board = conversion([list(input().strip()) for _ in range(3)])
    queue = deque([(board,0)])
    MAX = 0
    for i in range(10):
        MAX += (1 << i)
    visited = [0 for _ in range(MAX)]
    print(bfs())
