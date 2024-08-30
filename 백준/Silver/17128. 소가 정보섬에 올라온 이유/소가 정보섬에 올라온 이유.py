import sys
from collections import deque
input = sys.stdin.readline

N,Q = map(int,input().split())

score = deque(list(map(int,input().split())))
cows = list(map(int,input().split()))

score_sum = []
for i in range(N):
    tmp = 1
    for j in range(4):
        tmp*=score[j]
    score_sum.append(tmp)
    score.rotate(-1)
res = sum(score_sum)
for cow in cows:
    for i in range(4):
        score_sum[cow-1-i] = -score_sum[cow-1-i]
        res += (score_sum[cow-1-i]*2)
    print(res)