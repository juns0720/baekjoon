import sys
import heapq
input = sys.stdin.readline

N,H,T = map(int,input().split())
hp = []

for _ in range(N):
    heapq.heappush(hp,-int(input()))
cnt = 0

'''
종료 조건
2. 뿅망치 횟수를 다 썼으면 종료

풀이
1. 힙에서 꺼낸 원소가 1이 아니고 내 키보다 크다면 //2
'''
for i in range(T):
    height_giant = -heapq.heappop(hp)
    if height_giant > 1 and height_giant >= H:
        height_giant //= 2
        cnt+=1
        heapq.heappush(hp,-height_giant)
    else:
        heapq.heappush(hp,-height_giant)
        break

max_height_giant = -heapq.heappop(hp)
print("YES" + "\n" + str(cnt)) if max_height_giant < H else print("NO" + "\n" + str(max_height_giant))