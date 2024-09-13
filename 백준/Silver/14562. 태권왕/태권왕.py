import sys
from collections import deque
input = sys.stdin.readline

C = int(input())
def check():

    while queue:
        my_score,score2,cnt = queue.popleft()
        if my_score == score2:
            return cnt
        if my_score*2 <= score2+3:
            queue.append((my_score*2, score2+3, cnt+1))
        if my_score+1 <= score2:
            queue.append((my_score+1,score2,cnt+1))

for tc in range(C):
    S,T = map(int,input().split())
    queue = deque()
    queue.append((S,T,0))
    print(check())