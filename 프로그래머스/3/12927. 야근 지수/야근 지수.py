import heapq 

def solution(n, works):
    answer = 0
    
    hq = []
    for w in works:
        heapq.heappush(hq,-w)
    
    while hq and n > 0:
        work = -heapq.heappop(hq)
        work -= 1

        if work > 0:
            heapq.heappush(hq,-work)
        n -= 1
    
    while hq:
        w = -heapq.heappop(hq)
        answer += w**2
        
    
    return answer