import sys
input = sys.stdin.readline
MAX = int(1e9)*2
n,k = map(int,input().split())
lev = [int(input()) for _ in range(n)]

def binary_search():
    s = 1
    e = MAX + 1
    while s+1 < e:
        mid = (s+e)//2
        gap = 0
        for i in range(n):
            if lev[i] < mid:
                gap += abs(lev[i]-mid)
        if gap > k:
            e = mid
        else:
            s = mid
    return s
res = binary_search()
print(res)

