import sys
input = sys.stdin.readline

tc = int(input())

def binary_search(n, s, e):
    while s+1 < e:
        mid = (s + e) // 2
        if n > B[mid]:
            s = mid
        else:
            e = mid
    return s

for _ in range(tc):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = sorted(list(map(int,input().split())))
    res = 0
    for i in range(N):
        idx = binary_search(A[i], 0, M)
        if A[i] <= B[idx]:
            continue
        res += len(B[:idx+1])
    print(res)
