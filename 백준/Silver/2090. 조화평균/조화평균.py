import sys
import math
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lcm = lst[0]

for i in range(1,n):
    lcm = math.lcm(lcm,lst[i])

a = sum([(lcm//lst[i]) for i in range(n)])
gcd = math.gcd(lcm,a)
print(f'{lcm//gcd}/{a//gcd}')