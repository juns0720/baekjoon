import sys
input = sys.stdin.readline

n = int(input())
tlist = list(map(int,input().split()))
tlist.sort()
res = 0
if(n % 2 == 1):
    for i in range((n-1)//2):
        res = max(res, tlist[i] + tlist[n-2-i])
else:
    for i in range(n//2):
        res = max(res, tlist[i] + tlist[n-1-i])
print(res)
    