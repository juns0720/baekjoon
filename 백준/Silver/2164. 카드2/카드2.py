import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])

n = int(input())                # 1 2 3 4 5 6 카드가 있음

for i in range(1,n+1):
    queue.append(i)



while True:
    if len(queue) == 0:
        print('-1')
        break
    else:
        if len(queue) == 1:
            print(queue[0])
            break
        elif len(queue) == 2:
            queue.popleft()
        else:
            queue.popleft()
            t = queue.popleft()
            queue.append(t)
