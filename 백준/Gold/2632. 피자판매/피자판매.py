import sys
input = sys.stdin.readline

N = int(input())
m,n = map(int,input().split())

A, B = [int(input()) for _ in range(m)],[int(input()) for _ in range(n)]



pa,pb = {0:1}, {0:1}


pa[sum(A)] = 1
for i in range(m):
    size = 0
    for j in range(i,m+i-1):
        if i != j and A[i] + A[j%m] > N:
            continue

        size += A[j%m]
        if size in pa:
            pa[size] += 1
        else:
            pa[size] = 1

pb[sum(B)] = 1
for i in range(n):
    size = 0
    for j in range(i,n+i-1):
        if i != j and B[i] + B[j%n] > N:
            continue

        size += B[j%n]
        if size in pb:
            pb[size] += 1
        else:
            pb[size] = 1

def binary_search(target):
    s = 0
    e = len(pb_key)
    
    while s + 1 < e:
        mid = (s + e) // 2

        if pb_key[mid] + target <= N:
            s = mid
        else:
            e = mid

    return pb_key[s]

pb_key = sorted(list(pb.keys()))

cnt = 0
for i in pa.keys():
    j = binary_search(i)
    if i+j == N:
        cnt += pa[i]*pb[j]

print(cnt)