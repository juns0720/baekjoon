import sys
from math import isqrt
input = sys.stdin.readline
MAX_SIZE = 10**6+1
n = int(input())
arr = list(map(int,input().split()))


dic = {}
for i in range(n):
    tmp = arr[i]
    j = 2
    while tmp > 1:
        if tmp % j == 0:
            tmp = tmp // j
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        else:
            j += 1

max_value = 1
res = 0
for k,v in dic.items():
    pow = v // n
    if pow == 0:
        continue
    max_value *= k**pow
    for num in arr:
        cnt = 0
        for i in range(pow):
            if num % k != 0:
                break
            num //= k
            cnt += 1
        res += (pow - cnt)
print(max_value,res)