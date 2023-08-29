import sys
input = sys.stdin.readline

T = int(input())


def check(a,b):
    cnt = 0
    if arr[a][0] != arr[b][0]:
        cnt+=1
    if arr[a][1] != arr[b][1]:
        cnt+=1
    if arr[a][2] != arr[b][2]:
        cnt+=1
    if arr[a][3] != arr[b][3]:
        cnt+=1
    return cnt

for i in range(T):
    N = int(input())
    res = 4*N
    arr = list(input().split())
    if N > 32:
        res = 0
    else:
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    res = min(res,check(i,j)+check(j,k)+check(i,k))
    print(res)
