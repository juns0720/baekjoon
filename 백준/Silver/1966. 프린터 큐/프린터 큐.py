import sys
from collections import deque
input = sys.stdin.readline


for i in range(int(input())):
    N,M = map(int,input().split())  #6, 0
    cnt = 0
    queue = deque(list(map(int,input().split())))  #1 1 9 1 1 1
    index = M
    while True:
        if len(queue) == 0:
            break
        if max(queue) == queue[0]:
            cnt+=1
            queue.popleft()
            if index == 0:
                break
            else:
                index-=1
        else:
            temp = queue[0]
            queue.popleft()
            queue.append(temp)
            if index == 0:
                index = len(queue)-1
            else:   
                index-=1
    print(cnt)


    
    


