import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])
n = int(input())

for i in range(n):
    str = input().split()
    if str[0] =='push_front':
        queue.appendleft(str[1])
    elif str[0] =='push_back':
        queue.append(str[1])
    elif str[0] =='pop_front':
        if len(queue) == 0:
            print('-1')
        else :
            t = queue.popleft()
            print(t)

    elif str[0] =='pop_back':
         if len(queue) == 0:
            print('-1')
         else:
            t = queue.pop()
            print(t)

    elif str[0] == 'size':
        print(len(queue))
    elif str[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif str[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif str[0] == 'back':
        if len(queue) == 0:
            print('-1')       
        else:
            print(queue[-1]) 
