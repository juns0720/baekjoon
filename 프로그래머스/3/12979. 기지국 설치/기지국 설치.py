def solution(n, stations, w):
    answer = 0

    gaps = []
    
    for station in stations:
        s,e = max(0,station-w), min(station+w,n)

        gaps.append([s,e])
    
    seq = [gaps[0][0]-1, n - gaps[-1][1]]
    
    for i in range(1,len(gaps)):
        seq.append(gaps[i][0]-gaps[i-1][1]-1)
    
    r = 2*w+1
    
    for s in seq:
        answer += ((s+r-1) // r)
    

        
    
    return answer