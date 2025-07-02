import sys
input = sys.stdin.readline

board = [tuple(map(int,input().split())) for _ in range(5)]
answer = [tuple(map(int,input().split())) for _ in range(5)]
dic = {}

for i in range(5):
    dic[(board[i])] = 0

for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(board[j][i])
    dic[tuple(tmp)] = 0

tmp = []
for i in range(5):
    tmp.append(board[i][i])
dic[tuple(tmp)] = 0
dic[(board[4][0],board[3][1],board[2][2],board[1][3],board[0][4])] = 0
cnt = 0

for i in range(5):
    for j in range(5):
        n = answer[i][j]
        for k,v in dic.items():
            if n in k:
                if dic[k] == 4:
                    dic[k] = 5
                    cnt += 1
                dic[k] += 1
        if cnt > 2:
            print(i*5 + j+1)
            exit()
