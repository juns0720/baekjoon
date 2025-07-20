import sys
input = sys.stdin.readline

n = int(input())
pos = [list(map(int,input().split())) for _ in range(n)]

pos_x, pos_y = [], []
set_x, set_y = set(), set()

for i in range(n):
    x1, y1 = pos[i]
    x2, y2 = pos[(i+1)%n]

    if y1 == y2:
        x_start, x_end = sorted((x1, x2))
        pos_y.append((x_start, x_end - 1)) 
        for x in range(x_start, x_end):
            set_y.add(x)
    elif x1 == x2:
        y_start, y_end = sorted((y1, y2))
        pos_x.append((y_start, y_end - 1)) 
        for y in range(y_start, y_end):
            set_x.add(y)

set_x = sorted(set_x)
set_y = sorted(set_y)
dic_x = {v:i for i, v in enumerate(set_x)}
dic_y = {v:i for i, v in enumerate(set_y)}

prefix_x = [0] * (len(dic_x) + 2)
for y1, y2 in pos_x:
    prefix_x[dic_x[y1]] += 1
    prefix_x[dic_x[y2]+1] -= 1

prefix_y = [0] * (len(dic_y) + 2)
for x1, x2 in pos_y:
    prefix_y[dic_y[x1]] += 1
    prefix_y[dic_y[x2]+1] -= 1

res = 0
for i in range(1, len(prefix_x)):
    prefix_x[i] += prefix_x[i-1]
    res = max(res, prefix_x[i])

for i in range(1, len(prefix_y)):
    prefix_y[i] += prefix_y[i-1]
    res = max(res, prefix_y[i])

print(res)
