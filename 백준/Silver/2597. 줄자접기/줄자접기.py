import sys
input = sys.stdin.readline
length = int(input())
dot = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    if dot[i][0] == dot[i][1]:
        continue
    mid = sum(dot[i]) / 2
    length = max(length-mid, mid)
    for j in range(i+1,3):
        for k in range(2):
            dot[j][k] = abs(dot[j][k]-mid)
print(f'{length:.01f}')