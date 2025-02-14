import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
LIS = [arr[0]]

def binary_search(target):
    s = -1
    e = len(LIS)

    while s+1 < e:
        mid = (s+e)//2
        if LIS[mid] < target:
            s = mid
        else:
            e = mid
    return e

LIS_idx = [0]
for i in range(1,N):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
        LIS_idx.append(len(LIS)-1)
    else:
        idx = binary_search(arr[i])
        LIS[idx] = arr[i]
        LIS_idx.append(idx)

l = len(LIS)-1
res = []
for i in range(len(arr)-1,-1,-1):
    if LIS_idx[i] == l:
        res.append(arr[i])
        l-=1
        
res.reverse()
print(len(res))
print(*res)