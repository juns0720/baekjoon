import sys
input = sys.stdin.readline

A = [0] + list(input().strip())
B = [0] + list(input().strip())

len_A = len(A)
len_B = len(B)

board = [['' for _ in range(len_A)] for _ in range(len_B)]

for i in range(1, len_B) :
    for j in range(1, len_A) :
        if A[j] == B[i] :
            board[i][j] = board[i-1][j-1] + A[j]
        else :
            if len(board[i][j-1]) > len(board[i-1][j]) :
                board[i][j] = board[i][j-1]
            else : 
                board[i][j] = board[i-1][j]

print(len(board[-1][-1]), board[-1][-1],sep = '\n')