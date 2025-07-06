import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = [list(map(int,input().split())) for _ in range(N)]

heapq.heapify(hq)

com = []
hq2 = []
dic = {0:0}
max_i = 0
while hq:
    nst,net = heapq.heappop(hq)
    while hq2:
        et,st,i = heapq.heappop(hq2)
        if et <= nst:# 사용 종료
            heapq.heappush(com,i)
            continue
        else:
            heapq.heappush(hq2,(et,st,i))
            break
    if not com:
        dic[max_i] = 1
        ni = max_i
        max_i += 1
    else:
        ni = heapq.heappop(com)
        dic[ni] += 1
        
    heapq.heappush(hq2,(net,nst,ni))
print(len(dic))
print(*dic.values())