import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
T = int(input())
queue = deque(list(map(int,input().split())))
num = list(map(int,input().split()))
for i in range(T):
    for _ in range(num[i]-1):
        queue.append(queue.popleft())
    print(queue[0],end = ' ')