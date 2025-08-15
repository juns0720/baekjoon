import sys
input = sys.stdin.readline

N = 1000
board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(2):
    y1,x1,y2,x2 = map(int,input().split())
    for r in range(y1,y2+1):
        for c in range(x1,x2+1):
            board[r][c] += 1


py = set()
px = set()    
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            py.add(r)
            px.add(c)
if len(py) == 1 and len(px) == 1:
    print("POINT")
elif len(py) == 1 or len(px) == 1:
    print("LINE")
elif len(py) > 2 and len(px) > 2:
    print("FACE")
else:
    print("NULL")