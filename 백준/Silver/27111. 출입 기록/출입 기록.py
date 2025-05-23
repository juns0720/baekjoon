import sys
input = sys.stdin.readline

arr = [0 for _ in range(200001)]

cnt = 0

for i in range(int(input())):
    a,b = map(int,input().split())
    if b == 1:
        if arr[a] == 1:
            cnt += 1
        arr[a] = 1
    else:
        if arr[a] == 0:
            cnt += 1
        arr[a] = 0

for i in arr:
    cnt += i
print(cnt)
