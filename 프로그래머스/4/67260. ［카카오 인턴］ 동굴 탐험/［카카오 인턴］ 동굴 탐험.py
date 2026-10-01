from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    before = [-1] * n
    for a, b in order:
        before[b] = a
        
    if before[0] != -1:
        return False

    visited = [False] * n
    wait = [-1] * n
    visited[0] = True
    queue = deque([0])
    cnt = 1

    while queue:
        v1 = queue.popleft()
        
        if wait[v1] != -1:          
            v2 = wait[v1]
            visited[v2] = True
            queue.append(v2)
            cnt += 1
            
        for v2 in graph[v1]:
            if visited[v2]:
                continue
                
            if before[v2] != -1 and not visited[before[v2]]:
                wait[before[v2]] = v2
                continue
                
            visited[v2] = True
            queue.append(v2)
            cnt += 1

    return cnt == n