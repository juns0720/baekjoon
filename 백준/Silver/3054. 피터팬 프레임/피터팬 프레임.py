import sys
input = sys.stdin.readline

def make(n):
    idx = 2
    for i in range(1,n+1):
        board[2][idx] = s[i-1]
        if i % 3 == 0:
            for j in [idx-2,idx+2]:
                board[2][j] = '*'
        else:
            for j in [idx-2,idx+2]:
                if board[2][j] == '*':
                    continue
                board[2][j] = '#'
        idx += 4

    # 0, n-1줄
    for i in [0,4]:
        idx = 2
        for j in range(1,n+1):
            if j % 3 == 0:
                board[i][idx] = '*'
                if i == 0:
                    board[i+1][idx-1] = '*'
                    board[i+1][idx+1] = '*'
                else:
                    board[i-1][idx-1] = '*'
                    board[i-1][idx+1] = '*'
                
            else:
                board[i][idx] = '#'
                if i == 0:
                    board[i+1][idx-1] = '#'
                    board[i+1][idx+1] = '#'
                else:
                    board[i-1][idx-1] = '#'
                    board[i-1][idx+1] = '#'
            idx += 4
    
    


s = input().strip()
n = len(s)
board = [['.' for _ in range(4*n + 1)] for _ in range(5)]

make(n)
for i in board:
    for j in i:
        print(j, end='')
    print()