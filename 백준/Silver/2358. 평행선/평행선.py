import sys
from math import comb
input = sys.stdin.readline

n = int(input())
x_pos = {}
y_pos = {}
for i in range(n):
    y,x = map(int,input().split())
    if y not in y_pos:
        y_pos[y] = 1
    else:
        y_pos[y] += 1
    if x not in x_pos:
        x_pos[x] = 1
    else:
        x_pos[x] += 1
res = 0

for v in x_pos.values():
    if v > 1:
        res += 1
for v in y_pos.values():
    if v > 1:
        res += 1
print(res)
