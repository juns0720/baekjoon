a,b = map(int,input().split())
board = []
low = 0
column = 0
for i in range(a):
    board.append(list(input().strip()))

for i in range(a):
    if 'X' not in board[i]:
        low+=1

for i in range(b):
    tmp = 1
    for j in range(a):
        if board[j][i] == 'X':
            tmp = 0
            break
    column+=tmp
if low+1 > column:
    print(low)
else:
    print(column)
