import sys
input = sys.stdin.readline

n = int(input())

arr = [list(input().strip()) for _ in range(n)]
if n == 1:
    print(0)
    exit()
    
visited = []
for i in range(1,n+1):
    visited.append([0]*i)

for r in range(n-1,0,-1):
    for c in range(len(arr[r])):
        if visited[r][c]:
            continue
        #블루 제거
        if 0 < c < len(arr[r])-1 and arr[r][c] == 'B' and not visited[r][c]:
            if not visited[r-1][c-1] and not visited[r-1][c] and arr[r-1][c-1] == 'B' and arr[r-1][c] == 'B':
                visited[r][c], visited[r-1][c-1], visited[r-1][c] = 2,2,2
            else:
                print(0)
                exit()
        #레드 제거
        elif c+1 < len(arr[r]) and not visited[r][c] and arr[r][c] == 'R' and not visited[r][c+1]  and arr[r][c+1] == 'R':
            if not visited[r-1][c] and arr[r-1][c] == 'R':
                visited[r][c], visited[r][c+1], visited[r-1][c] = 1,1,1
        else:
            print(0)
            exit()

print(1)