import sys
import math
input = sys.stdin.readline

a,b = map(int,input().split())

arr = []

for i in range(1, int(b**0.5) + 1):
    if b % i == 0:
        arr.append(i)

for i in arr[::-1]:
    arr.append(b//i)

res = [b, b]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if math.gcd(arr[i],arr[j]) == a and math.lcm(arr[i],arr[j]) == b:
            if arr[i] + arr[j] < sum(res):
                res = [arr[i], arr[j]]

print(*res)