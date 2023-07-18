import sys
import heapq
input = sys.stdin.readline

N = int(input())
lecture = []
for _ in range(N):    
    heapq.heappush(lecture,list(map(int,input().split())))
lecture.sort()
check = []

heapq.heappush(check,lecture[0][1])
for i in range(1,N):
    if  check[0] <= lecture[i][0]:   # 이어질 수 있을 때
        heapq.heappop(check)    #원래 강의 시간 업데이트
        heapq.heappush(check,lecture[i][1])
    else:   #이어질 수 없을 때
        heapq.heappush(check,lecture[i][1])
print(len(check))