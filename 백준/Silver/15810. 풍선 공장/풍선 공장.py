import sys
input = sys.stdin.readline
MAX = int(1e12)
N,M = map(int,input().split())
times = list(map(int,input().split()))


s = 0
e = MAX
while s+1 < e:
    mid = (s+e) // 2
    cnt = 0
    for time in times:
        cnt += (mid // time)
    if cnt < M:
        s = mid
    else:
        e = mid
print(e)