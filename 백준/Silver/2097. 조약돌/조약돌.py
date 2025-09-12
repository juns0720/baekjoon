import sys
from math import ceil
input = sys.stdin.readline

n = int(input())

if n < 5:
    print(4)
    exit()
a = ceil(n ** 0.5)
b = ceil(n / a)
print((a+b-2)*2)