import sys
input = sys.stdin.readline


    
for tc in range(1, int(input())+1):
    print("Case " + str(tc)+": ",end='')
    board = []
    for i in range(9):
        lst = list(map(int,input().split()))
        if not lst:
            lst = list(map(int,input().split()))
        board.append(lst)

    flag = True
    #가로
    for row in range(9):
        if len(set(board[row])) != 9:
            flag = False
            break

    if not flag:
        print("INCORRECT")
        continue

    #세로
    for col in range(9):
        tmp = set()
        for row in range(9):
            tmp.add(board[row][col])
        if len(tmp) != 9:   
            flag = False
            break

    if not flag:
        print("INCORRECT")
        continue
    #3x3
    dy = [0,3,6]
    dx = [0,3,6]
    for y in dy:
        for x in dx:
            tmp = set()
            for row in range(x,x+3):
                for col in range(y,y+3):
                    tmp.add(board[row][col])
            if len(tmp) != 9:   
                flag = False
                break
    if not flag:
        print("INCORRECT")
        continue
    print("CORRECT")