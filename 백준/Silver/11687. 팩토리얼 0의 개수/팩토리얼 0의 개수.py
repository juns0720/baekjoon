import sys
from math import log
input = sys.stdin.readline

M = int(input())

def cal(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n //= 5
    return cnt

s, e = 1, 5 * M
while s + 1 < e:
    mid = (s + e) // 2

    cnt = cal(mid)

    if cnt < M:
        s = mid
    else:
        e = mid
res = cal(e)
print(e if res == M else -1)
