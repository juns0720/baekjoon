import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().strip())
c = 0
f = 0
for i in arr:
    if i == 'C':
        c += 1
    else:
        f += 1
res = c
for i in range(c+1):
    res = min(res,max(i,c-i*f))
print(res)
