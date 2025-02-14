import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dot = sorted(list(map(int,input().split())))


def binary_search(s,e,target):
    while s+1 < e:
        mid = (s+e)//2
        if target < dot[mid]:
            e = mid
        else:
            s = mid
    return s




for _ in range(M):
    l,r = map(int,input().split())
    s = (binary_search(0,len(dot),l))
    e = (binary_search(0,len(dot),r))
    res = e-s+1
    if s == e:
        if l <= dot[s] <= e:
            res = 1
        else:
            res = 0
    else:
        if dot[s] < l:
            res -= 1
        if dot[e] > r:
            res -= 1
    print(res)