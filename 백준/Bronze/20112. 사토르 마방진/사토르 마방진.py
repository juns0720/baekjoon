import sys
input = sys.stdin.readline
n = int(input())

board = [list(input().strip()) for _ in range(n)]

for i in range(n):
    a = ''.join(board[i])
    b = []
    for j in range(n):
        b.append(board[j][i])
    b = ''.join(b)
    if a != b:
        print("NO")
        exit()
print("YES")