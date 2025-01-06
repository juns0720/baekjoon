import sys
input = sys.stdin.readline

R,C = map(int,input().split())


board = [list(input().strip())+["#"] for _ in range(R) ]
board.append(['#' for _ in range(C)])
words = []

#가로 단어 검사
for row in range(R):
    word = []
    for col in range(C+1):
        if board[row][col] == '#':
            if len(word) > 1:
                words.append("".join(word))
            word.clear()
        else:
            word.append(board[row][col])

for col in range(C):
    word = []
    for row in range(R+1):
        if board[row][col] == '#':
            if len(word) > 1:
                words.append("".join(word))
            word.clear()
        else:
            word.append(board[row][col])


print(sorted(words)[0])