import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
res = 1
def check():
    res = 1
    for y in range(N):
        cnty = 1
        cntx = 1
        for x in range(1,N):
            if arr[x][y] != arr[x-1][y]:
                cnty = 1
            else:
                cnty+=1
            res = max(cnty,res)
        for x in range(1,N):
            if arr[y][x] != arr[y][x-1]:
                cntx = 1
            else:
                cntx+=1
            res = max(cntx,res)
    return res
for y in range(N):
    for x in range(N):
        if y+1 < N: #열 바꾸기
            if arr[y][x] != arr[y+1][x]:
                arr[y][x],arr[y+1][x] = arr[y+1][x], arr[y][x]
                res = max(res,check())
                arr[y][x],arr[y+1][x] = arr[y+1][x], arr[y][x]
        if x+1 < N: #행 바꾸기
            if arr[y][x] != arr[y][x+1]:
                arr[y][x],arr[y][x+1] = arr[y][x+1], arr[y][x]
                res = max(res,check())
                arr[y][x],arr[y][x+1] = arr[y][x+1], arr[y][x]
print(res)