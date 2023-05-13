import sys
input = sys.stdin.readline

nl = []
for _ in range(9):
    nl.append(list(map(int,input().split())))

max_n = -1
x,y = 0,0
for i in range(9):
    for j in range(9):
        if nl[i][j] > max_n:
            max_n = nl[i][j]
            y = i+1
            x = j+1
print(max_n)
print(y, x)


