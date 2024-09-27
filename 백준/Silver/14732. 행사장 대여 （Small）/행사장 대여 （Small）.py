import sys
input = sys.stdin.readline

N = int(input())


board = [[0 for _ in range(500)] for _ in range(500)]
res = 0

for i in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            board[j][k]+=1
for row in range(500):
    for col in range(500):
        if board[row][col] > 0:
            res+=1
print(res)