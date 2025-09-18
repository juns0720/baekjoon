import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

total_len = sum(len(s) for s in arr)
req = m - total_len

res = [req // (n-1)] * (n-1)
extra = req % (n-1)

for i in range(n-1):
    if extra > 0 and arr[i+1][0].islower():
        res[i] += 1
        extra -= 1

for i in range(n-2, -1, -1):
    if extra > 0 and arr[i+1][0].isupper():
        res[i] += 1
        extra -= 1

for i in range(n):
    print(arr[i], end="")
    if i < n-1:
        print("_" * res[i], end="")
