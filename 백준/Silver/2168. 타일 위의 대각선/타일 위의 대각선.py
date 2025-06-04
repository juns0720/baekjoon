import sys
from math import gcd
input = sys.stdin.readline

a,b = map(int,input().split())

res = a + b-gcd(a,b)
print(res)