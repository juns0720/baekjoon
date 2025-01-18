import sys
import heapq
input = sys.stdin.readline

def to_str(arr):
    return ''.join(arr)

def to_arr (str):
    return list(str)


n = int(input())
lst = list(input().split())
for i in range(n):
    lst[i] = str(int(lst[i])-1)
m = int(input())
command = []
for i in range(m):
    a,b,cost = map(int,input().split())
    command.append((a-1,b-1,cost))

start = to_str(lst)
goal = to_str(sorted(lst))
dic = {start : 0}

hq = []
heapq.heappush(hq,(dic[start],start))

while hq:
    cost, node = heapq.heappop(hq)
    if dic[node] < cost:
        continue
    for a,b,cur_cost in command:
        arr = to_arr(node)
        arr[a], arr[b] = arr[b], arr[a]
        arr = to_str(arr)
        if arr not in dic or dic[arr] > cost + cur_cost:
            dic[arr] = cost + cur_cost
            heapq.heappush(hq,(dic[arr],arr))

if goal in dic:
    print(dic[goal])
else:
    print(-1)