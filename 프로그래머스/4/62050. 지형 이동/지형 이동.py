from collections import deque

def solution(land, height):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    answer = 0
    N = len(land)
    
    
    def bfs(cnt):
        
        while queue:
            y,x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 or visited[ny][nx]:
                    continue
                if abs(land[y][x] - land[ny][nx]) > height:
                    continue
                board[ny][nx] = cnt
                visited[ny][nx] = 1
                queue.append((ny,nx))
                
    visited = [[0 for _ in range(N)] for _ in range(N)]
    board = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                queue = deque([(y,x)])
                board[y][x] = cnt
                visited[y][x] = 1
                bfs(cnt)
                cnt += 1
    
    dic = dict()
    
    for y in range(N):
        for x in range(N):
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 or board[y][x] == board[ny][nx]:
                    continue
                h = abs(land[y][x] - land[ny][nx])
                a = min(board[y][x], board[ny][nx])
                b = max(board[y][x], board[ny][nx])
                
                if (a,b) in dic:
                    dic[(a,b)] = min(dic[(a,b)], h)
                else:
                    dic[(a,b)] = h
    lst = deque(sorted(list(dic.items()), key = lambda x: x[1]))
    
    parent = [i for i in range(cnt)]
        
    def union(v1,v2):
        v1 = find(v1)     
        v2 = find(v2)

        if v1 > v2:
            parent[v1] = v2
        else:
            parent[v2] = v1
        
    
    def find(v1):
        if v1 != parent[v1]:
            parent[v1] = find(parent[v1])
            
        return parent[v1]

    while lst and cnt > 0:
        (v1,v2),v = lst.popleft()
        if find(v1) != find(v2):
            union(v1,v2)
            answer += v
            cnt -= 1
        
    return answer