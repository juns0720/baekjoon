import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])      #사람수 7, 3번째 제거
n = list(map(int,input().split()))

l = [str(i) for i in range(1,(n[0])+1)]
count = n[1]-1
while True:

    if len(l) == 0:
        break
    else:
        if count < len(l):
            queue.append(l[count])
            l.pop(count)
            count+=(n[1]-1)            
        elif count >= len(l):
             count-=len(l)
    if len(queue) == n[0]:
        break

print("<",', '.join(queue),">", sep="")
