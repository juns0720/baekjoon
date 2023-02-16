import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = list(map(int,input().split()))
queue2 = []
nl  = []
cnt = 0
for i in range(1,n+1):
    nl.append(i)

queue2.append(nl.pop(cnt))
bn = queue.pop(cnt)            #풍선 숫자

while queue :
    if bn < 0:
        cnt = (cnt+bn)%len(queue)
    else:
        cnt = (cnt+bn-1)%len(queue)
    bn = queue.pop(cnt)
    queue2.append(nl.pop(cnt))

a = ' '.join(str(i) for i in queue2)
print(a)

