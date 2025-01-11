import sys
from itertools import combinations
input = sys.stdin.readline

MAX = 9001

def make_prime():
    prime = [i for i in range(MAX)]
    prime[1] = 0
    for i in range(2, MAX):
        for j in range(i*2, MAX, i):
            prime[j] = 0
    return prime

N,M = map(int,input().split())
cows = list(map(int,input().split()))
prime = make_prime()
res = set()
for selected in combinations(cows,M):
    weight = sum(selected)
    if prime[weight]:
        res.add(weight)
if not res:
    print(-1)
else:
    print(*sorted(res))