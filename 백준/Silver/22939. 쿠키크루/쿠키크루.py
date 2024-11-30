import sys
from itertools import permutations
input = sys.stdin.readline

topping = [[] for _ in range(4)]
key = [('J',"Assassin"),('C',"Healer"),('B',"Mage"),('W',"Tanker")]
dist = [int(1e9) for _ in range(4)]
n = int(input())

board =[list(input().strip()) for _ in range(n)]


for row in range(n):
    for col in range(n):
        if board[row][col] == 'H':
            sy,sx = row,col
        elif board[row][col] == '#':
            ey,ex = row,col
        for i in range(4):
            if board[row][col] == key[i][0]:
                topping[i].append((row,col))
                break

for i in range(4):
    for pmt in permutations(topping[i],3):
        cur_dist = 0
        tmp = [(sy,sx)] + list(pmt) + [(ey,ex)]
        for j in range(1,5):
            cur_dist += abs(tmp[j][0]-tmp[j-1][0]) + abs(tmp[j][1]-tmp[j-1][1])
        dist[i] = min(dist[i], cur_dist)

res = [dist[0],key[0][1]]

for i in range(1,4):
    if dist[i] < res[0]:
        res = [dist[i], key[i][1]]
print(res[1])
