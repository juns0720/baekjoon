import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int,input().split()))
t,p = map(int,input().split())

res = 0

for i in size:
    cnt = i // t
    if i % t != 0:
        res += cnt + 1
    else:
        res += cnt
print(res)
print(n // p, n % p)