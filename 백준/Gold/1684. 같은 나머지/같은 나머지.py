import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
res = 0
for i in range(1001):
    for j in range(N):
        arr[j] += i
    tmp = arr[0]
    for j in range(1,N):
        tmp = gcd(tmp,arr[j])
    res = max(tmp,res)
    for j in range(N):
        arr[j] -= i
print(res)