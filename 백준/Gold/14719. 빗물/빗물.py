import sys
input = sys.stdin.readline

H,W = map(int,input().split())
arr = list(map(int,input().split()))
res = 0
for i in range(1,W-1):
    l,r = max(arr[:i]),max(arr[i:])# 좌우 높은 기둥
    Min = min(l,r) #더 작은기둥
    if arr[i] < Min:
        res+=(Min-arr[i])
print(res)