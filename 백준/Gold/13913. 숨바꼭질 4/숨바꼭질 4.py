# import sys
# from collections import deque
# input = sys.stdin.readline

# N,K = map(int,input().split())
# graph = [abs(K-N) for _ in range((K+N)*2+1)]
# sequence = [0 for _ in range(100001)]
# visited = [0 for _ in range((K+N)*2+1)]
# graph[N] = 0
# queue = deque([(N,-1)])
# def BFS():
#     while queue:
#         n, prev_pos = queue.popleft()

#         visited[n] = 1
#         dn = [n,-1,1]
#         for i in range(3):
#             tn = n+dn[i]
#             if tn > -1 and tn < K*2+1 and not visited[tn]:
#                 queue.append((tn, n))
#                 visited[tn] = 1
#                 graph[tn] = min(graph[n]+1,graph[tn])
#     print(graph[K])

# BFS()


from collections import deque
import sys
input = sys.stdin.readline

def hide_and_seek():
    while(queue):
        current, prev_pos = queue.popleft()
        if not sequence[current]:
            sequence[current] = prev_pos
        # 동생을 찾으면 걸린 시간을 반환한다
        if (current == k):
            pos = k
            while pos != -1:
                result.append(pos)
                pos = sequence[pos]

            return time[current]
        
        
        # 수빈이가 이동할 수 있는 경우의 수 3가지
        for next in [current + 1, current -1, current * 2]:
            if (next < 0 or next > 100_000 or visited[next]):
                continue

            # 순간이동을 하면 1초 후에 (현재위치 * 2)로 이동한다
            # 걸으면 1초 후에 (현재위치 - 1) 또는 (현재위치 + 1)로 이동한다=
            queue.append((next, current))
            visited[next] = True
            time[next] = time[current] + 1

n, k = map(int, input().split()) # 수빈이가 있는 위치, 동생이 있는 위치

queue = deque([(n,-1)])
time = [0] * 100_001
visited = [False] * 100_001
sequence = [0] * 200_001
result = []
print(hide_and_seek())
print(*result[::-1])
