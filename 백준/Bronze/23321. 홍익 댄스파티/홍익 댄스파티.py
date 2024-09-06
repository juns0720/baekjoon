import sys
input = sys.stdin.readline


tmp = [['.','o','.'],
       ['o','w','.'],
       ['m','l','o'],
       ['l','n','L'],
       ['n','.','n']]

lst = [list(input().strip()) for _ in range(5)]
s_type = [0 for _ in range(len(lst[0]))]

for col in range(len(lst[0])):
    for row in range(5):
        if lst[row][col] == 'w':
            s_type[col] = 1
        elif lst[row][col] == 'L':
            s_type[col] = 2

for i in range(5):
    for j in range(len(lst[i])):
        if s_type[j] == 0:
            print(tmp[i][1],end='')
        elif s_type[j] == 1:
            print(tmp[i][0],end='')
        else:
            print(tmp[i][2],end='')
    print()
            