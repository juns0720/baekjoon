import sys
import math
input = sys.stdin.readline


def cal(n):
    if n == 1:
        return
    i = num[1] // num[0]
    if num[1] % num[0] > 0:
        i+=1
    lcm = math.lcm(i,num[1])
    num[0] = (num[0] * (lcm//num[1]))-(lcm // i)
    num[1] = lcm

    gcd = math.gcd(num[0],num[1])
    for i in range(2):
        num[i] //= gcd

    cal(num[0])

for tc in range(int(input())):
    num = list(map(int,input().split()))
    gcd = math.gcd(num[0],num[1])
    for i in range(2):
        num[i] //= gcd
    cal(num[0])
    print(num[1])
