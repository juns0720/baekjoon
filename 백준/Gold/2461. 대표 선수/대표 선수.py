import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())


seq = []
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(M):
        seq.append([tmp[j],i])

seq.sort()
arr = [-1 for _ in range(N)]

res = int(1e10)
for i in range(len(seq)):
    arr[seq[i][1]] = seq[i][0]
    if -1 not in arr:
        res = min(res, max(arr)-min(arr))

print(res)