import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

if N in [1,2]:
    print(N)
    exit()

A.sort()
res = 2
for i in range(N-1):
    x,y = A[i], A[i+1]

    for j in range(i+2,N):
        z = A[j]

        if x+y <= z:
            break
        res = max(res, j-i+1)

print(res)