import sys
from math import ceil
input = sys.stdin.readline

n = int(input())
res = 1
i = 1
while i < n:
    cnt = ceil(n/i)
    gap = cnt - 1

    tmp = (n // i)
    if n % i == 0:
        max_val = i*(tmp-1) + 1
    else:
        max_val = i*tmp + 1
    total = ceil((n-max_val+1) / gap)

    res += cnt * total
    i += total
print(res)