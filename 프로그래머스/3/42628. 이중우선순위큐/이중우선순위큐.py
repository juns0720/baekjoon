import heapq


def solution(operations):
    answer = [0,0]     
    min_hq = []
    max_hq = []
    
    visited = dict()
    for o in operations:
        o = o.split()
        
        if o[0] == 'I':
            heapq.heappush(min_hq, int(o[1]))
            heapq.heappush(max_hq, -int(o[1]))
            
            visited[int(o[1])] = 1
            
        else:
            if o[1] == '1':
                while max_hq:
                    mxv = -heapq.heappop(max_hq)
                    if visited[mxv]:
                        visited[mxv] = 0
                        break
            
            else:
                    while min_hq:
                        mnv = heapq.heappop(min_hq)
                        if visited[mnv]:
                            visited[mnv] = 0
                            break

    while min_hq:
        mnv = heapq.heappop(min_hq)
        if visited[mnv]:
            answer[1] = mnv
            break
                
    while max_hq:
        mxv = -heapq.heappop(max_hq)
        if visited[mxv]:
            answer[0] = mxv
            break
    
   
    return answer