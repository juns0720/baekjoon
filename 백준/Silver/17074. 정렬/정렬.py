import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

tmp = []
for i in range(1,n):
    if arr[i] < arr[i-1]:
        tmp.append(i)

if len(tmp) > 1:
    print(0)
    exit()
elif len(tmp) == 0:
    print(n)
    exit()

i = tmp[0]
cnt = 0
for j in [i-1,i]:
    if j < 0 or j > n-1:
        continue
    if j == 0:
        if n < 3:
            cnt += 1
            continue
        if arr[j+1] <= arr[j+2]:
            cnt += 1
    elif j == n-1:
        if n < 3:
            cnt += 1
            continue
        if arr[j-2] <= arr[j-1]:
            cnt += 1
    elif arr[j-1] <= arr[j+1]:
        cnt += 1


print(cnt)