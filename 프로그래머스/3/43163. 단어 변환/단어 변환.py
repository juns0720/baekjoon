
from collections import deque

def solution(begin, target, words):
    

    target = list(target)
    queue = deque([[list(begin),0]])

    visited = {begin: 1}
    
    words = {w : 1 for w in words}
    cnt = 0
    
    while queue:
        S, cnt = queue.popleft()

        if S == target:
            return cnt
            
        for i in range(len(S)):
            w = S[i]
            
            for j in range(97,123):
                S[i] = chr(j)
                ns = ''.join(S)
                
                if ns in visited:
                    continue
                visited[ns] = 1
                
                if ns in words:
                    queue.append([list(ns), cnt+1])

            S[i] = w
    return 0