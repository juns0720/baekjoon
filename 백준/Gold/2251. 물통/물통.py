import sys
from collections import deque
A,B,C = map(int,input().split())
a,b,c = 0,0,C
visited = [[0 for _ in range(A+C)] for _ in range(B+C)]
visited[a][b] = 1
queue = deque([(a,b)])
res = []
def check():
    while queue:
        a,b = queue.popleft()
        c = C-a-b
        if a == 0:
            res.append(c)
        t = min(B-b,a)          # A->B
        if not visited[a-t][b+t]:
            queue.append((a-t,b+t))
            visited[a-t][b+t] = 1
        
        t = min(A-a,b)          # B->A
        if not visited[a+t][b-t]:
            queue.append((a+t,b-t))
            visited[a+t][b-t] = 1 

        t = min(C-c,a)          # A->C
        if not visited[a-t][b]:
            queue.append((a-t,b))
            visited[a-t][b] = 1

        t = min(A-a,c)          # C->A
        if not visited[a+t][b]:
            queue.append((a+t,b))
            visited[a+t][b] = 1

        t = min(C-c,b)          # B->C
        if not visited[a][b-t]:
            queue.append((a,b-t))
            visited[a][b-t] = 1

        t = min(B-b,c)          # C->B
        if not visited[a][b+t]:
            queue.append((a,b+t))
            visited[a][b+t] = 1
            
check()
print(*(sorted(res)))