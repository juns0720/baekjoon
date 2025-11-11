import sys
import math
input = sys.stdin.readline

N = int(input())

sum = 0

for i in range(N):
    score = list(input().strip())
    if score != ['1','0','0']:
        for i in range(len(score)):
            if score[i] in ['0','6','9']:
                score[i] = '9'

    sum += int(''.join(score))

res = sum / N

if res >= int(res) + 0.5:
    print(math.ceil(res))
else:
    print(int(res))