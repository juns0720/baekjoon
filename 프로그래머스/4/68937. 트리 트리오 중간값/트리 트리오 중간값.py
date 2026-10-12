import heapq
import sys

def solution(n, edges):
    answer = 0
    INF = sys.maxsize
    
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def dijkstra(v1):
        hq = []
        dist = [INF for _ in range(n+1)]
        dist[v1] = 0
        heapq.heappush(hq,(0, v1))
        
        while hq:
            cur_dist, v1 = heapq.heappop(hq)
            
            if cur_dist > dist[v1]:
                continue
            
            for v2 in graph[v1]:
                if dist[v2] <= dist[v1]+1:
                    continue
                
                dist[v2] = dist[v1]+1
                heapq.heappush(hq,(dist[v2],v2))
        return dist
        
    def find(dist):
        mv, md = 0, 0
        for v in range(1, n + 1):
            if dist[v] > md:
                mv, md = v, dist[v]
        return mv, md
    
    v1,a = find(dijkstra(1))
    
    dist1 = dijkstra(v1)
    v2,a = find(dist1)
    
    dist2 = dijkstra(v2)
    
    for v in range(1,n+1):
        if v in (v1,v2):
            continue
            
        answer = max(sorted([a,dist1[v],dist2[v]])[1], answer)
    
    return answer