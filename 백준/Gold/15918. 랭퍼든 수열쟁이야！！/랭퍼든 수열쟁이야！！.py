import sys
input = sys.stdin.readline

n,x,y = map(int,input().split())


arr = [0 for _ in range(2*n)]
visited = [0 for _ in range(n+1)]
s = y-x-1

visited[s] = 1
arr[x-1] = s
arr[y-1] = s
res = 0
def recursion(idx):
    global res
    if idx == 2*n:
        res += 1
        return
    
    if idx > 2*n-1:
        return
    if arr[idx] != 0:
        recursion(idx+1)
        return
    
    for i in range(1,n+1):
        if visited[i] or idx+i+1 > 2*n-1:
            continue

        if arr[idx] == 0 and arr[idx+i+1] == 0:
            arr[idx] = i
            arr[idx+i+1] = i
            visited[i] = 1
            recursion(idx+1)
            arr[idx] = 0
            arr[idx+i+1] = 0
            visited[i] = 0

recursion(0)
print(res)