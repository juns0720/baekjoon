import sys
import math
input = sys.stdin.readline

L = int(input())
lst = list(map(int,input().split()))

matrix = [[0 for _ in range(10)] for _ in range(10)]
matrix[1][3], matrix[1][7], matrix[3][9], matrix[7][9] = 2, 4, 6, 8
matrix[3][1], matrix[7][1], matrix[9][3], matrix[9][7] = 2, 4, 6, 8
matrix[1][9], matrix[3][7], matrix[2][8], matrix[4][6] = 5, 5, 5, 5
matrix[9][1], matrix[7][3], matrix[8][2], matrix[6][4] = 5, 5, 5, 5

visited = [0 for _ in range(10)]

prev = lst[0]
visited[prev] = 1
for cur_node in lst[1:]:
    if not matrix[prev][cur_node] and not visited[cur_node]:
        visited[cur_node] = 1
    elif matrix[prev][cur_node] and visited[matrix[prev][cur_node]]:
        visited[cur_node] = 1
    else:
        print("NO")
        exit()
    prev = cur_node
print("YES")
