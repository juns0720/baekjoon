from collections import deque

def solution(n, computers):
    
    def bfs():
        while queue:
            v1 = queue.popleft()
        
            for v2,connect in enumerate(computers[v1]):
                if visited[v2] or v1 == v2:
                    continue
                if connect:
                    queue.append(v2)
                    visited[v2] = 1
        return 1
    
    
    visited = [0 for _ in range(n)]
    answer = 0
    
    for v in range(n):
        if not visited[v]:
            queue = deque([v])
            visited[v] = 1
            answer += bfs()
    
    

    return answer