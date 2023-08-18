N,M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
for i in board:
    for j in range(1,len(i)+1):
        print(i[-j],end='')
    print('')