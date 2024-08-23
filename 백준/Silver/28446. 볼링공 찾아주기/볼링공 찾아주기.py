import sys
input = sys.stdin.readline

M = int(input())

balls = dict()

for tc in range(M):
    order = list(map(int,input().split()))
    if order[0] == 1:
        balls[order[2]] = order[1]
    else:
        print(balls[order[1]])