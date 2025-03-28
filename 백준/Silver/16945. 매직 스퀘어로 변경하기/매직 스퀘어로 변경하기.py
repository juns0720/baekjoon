import sys
from itertools import permutations
input = sys.stdin.readline

def check(board):
    values = set()
    #가로
    for r in range(3):
        values.add(sum(board[r]))

    #세로
    for c in range(3):
        values.add(sum([board[r][c] for r in range(3)]))

    #대각선
    values.add(sum([board[i][i] for i in range(3)]))
    values.add(board[2][0] + board[1][1] + board[0][2])

    return len(values)



board = [list(map(int,input().split())) for _ in range(3)]
tmp_board = []
for i in range(3):
    tmp_board += board[i]

res = sys.maxsize
for lst in list(permutations([i for i in range(1,10)])):
    cost = 0
    if check([lst[0:3],lst[3:6],lst[6:9]]) != 1:
        continue

    for i in range(9):
        cost += abs(tmp_board[i] - lst[i])

    res = min(cost, res)
    
print(res)
