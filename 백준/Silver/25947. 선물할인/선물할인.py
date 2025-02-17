import sys
input = sys.stdin.readline

n,b,a = map(int,input().split())
gift = sorted(list(map(int,input().split())))

prefix = [0 for _ in range(n)]
prefix[0] = gift[0]
for i in range(1,n):
    prefix[i] = prefix[i-1] + gift[i]

res = 0
if a == 0:
    for i in range(n):
        if prefix[i] <= b:
            res = i+1
        else:
            break

else:

    for i in range(a-1,-1,-1):
        if prefix[i]//2 <= b:
            res = i+1
            break

    for i in range(n-1,a-1,-1):
        total = prefix[i-a] + (prefix[i] - prefix[i-a]) // 2
        if total <= b:
            res = i+1
            break
print(res)