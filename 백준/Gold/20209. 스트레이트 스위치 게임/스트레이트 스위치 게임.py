import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
startNode = ''.join(input().split())
switch = [list(map(int,input().split()))[1:] for _ in range(K)]

for i in range(N-1):
    if startNode[i] != startNode[i+1]:
        break
else:
    print(0)
    exit()

queue = deque([(startNode)])
visited = {startNode: 0}
def bfs():
    
    while queue:
        v1 = queue.popleft()
    
        for idx,s in enumerate(switch):
            tmp = list(map(int,v1))
            for i in s:
                tmp[i-1] = (tmp[i-1]+idx+1) % 5
            
            v2 = ''.join(list(map(str,tmp)))

            if v2 in visited:
                continue
            
            visited[v2] = visited[v1]+1
            queue.append(v2)

            for i in range(N-1):
                if tmp[i] != tmp[i+1]:
                    break
            else:
                return visited[v2]
        
    return -1

print(bfs())