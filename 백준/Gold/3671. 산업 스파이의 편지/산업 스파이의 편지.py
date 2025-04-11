import sys
from itertools import permutations
from math import isqrt
input = sys.stdin.readline
MAX = int(1e7)
def make_prime():
    prime = [i for i in range(MAX)]
    prime[1] = 0
    for i in range(2,MAX):
        if not prime[i]:
            continue
        for j in range(i*i,MAX,i):
            prime[j] = 0
    return prime


prime = make_prime()
s = ['1','2']

for tc in range(int(input())):
    target = list(input().strip())
    res = 0
    visited = dict()
    for i in range(1,len(target)+1):
        for j in list(permutations(target,i)):
            num = int(''.join(j))
            if prime[num] and num not in visited:
                res+=1
                visited[num] = 1
    print(res)