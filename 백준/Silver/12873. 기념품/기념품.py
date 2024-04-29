import sys
from collections import deque
input = sys.stdin.readline

total_people = int(input())
player = deque([i for i in range(1, total_people+1)])
t = 1
while t!=total_people:
    index = t**3 % len(player)
    if index == 1: #첫번째 사람이면
        player.popleft()
    else: # 첫번째가 아닐 경우
        player.rotate(-(index-1)) #현재 큐에서 index번째 사람이 탈락자 이므로 popleft할 수 있도록 왼쪽으로 index-1번만큼 밀어준다.
        player.popleft()
    t+=1
print(player.popleft())
