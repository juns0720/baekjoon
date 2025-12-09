import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

res = 0

for i in range(N):
    for j in range(i+1, N):
        cnt = 0
        for k in range(N):
            if arr[i][k] and arr[j][k]:
                cnt += 1
                
        if cnt >= 2:
            res += cnt *(cnt-1) // 2 * 4

print(res)