import sys
from math import gcd, isqrt
input = sys.stdin.readline




R,G = map(int,input().split())

n = gcd(R,G)
arr = []
for i in range(1, isqrt(n)+1):
    if n % i == 0:
        arr.append(i)
        if n // i == i:
            continue
        arr.append(n//i)

for i in arr:
    print(i,R//i,G//i)