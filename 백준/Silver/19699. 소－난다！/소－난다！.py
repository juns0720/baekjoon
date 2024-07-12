import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
cows = list(map(int,input().split()))

def check(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


res = set()
for selected_cows in combinations(cows, M):
    sum_weight = sum(selected_cows)
    if check(sum_weight):
        res.add(sum_weight)
if not res:
    print(-1)
else:
    res = sorted(list(res))
    print(*res)
