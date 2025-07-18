import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

N = len(str(n))
queue = deque([[str(n),0]])
visited = [0 for _ in range(10**6+1)]

res = -1
def bfs():
    global res
    while queue:
        arr,cnt = queue.popleft()
        if cnt == k:
            res = max(res, int(arr))
            continue
        arr = list(arr)
        prev_arr = ''.join(arr)
        if visited[int(prev_arr)]:
            queue.append((str(visited[int(prev_arr)]),cnt + 1))
            continue
        max_value = 0
        for i in range(N):
            for j in range(i+1,N):
                if i == j or (i == 0 and arr[j] == '0'):
                    continue
                arr[i],arr[j] = arr[j], arr[i]
                curr_arr = ''.join(arr)
                if int(curr_arr) > max_value:
                    max_value = int(curr_arr)
                queue.append((''.join(arr),cnt+1))
                arr[i],arr[j] = arr[j],arr[i]
        visited[int(prev_arr)] = max_value
bfs()
print(res)