import sys
input = sys.stdin.readline

n = int(input())

lst =list(map(int,input().split()))

prefix = [0 for _ in range(n+1)]

prefix[0] = lst[0]
for i in range(1,n):
    prefix[i] = prefix[i-1] + lst[i]

res = 0
for i in range(n-1):
    res += lst[i] * (prefix[n-1]-prefix[i])
print(res)