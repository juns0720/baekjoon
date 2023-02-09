import sys
from collections import deque
input = sys.stdin.readline

n = list(map(int,input().split()))

queue = deque([])

for i in range(1,n[0]+1):
    queue.append(i)

t = list(map(int,input().split()))
ans = 0
count = 0
for i in t:
    if queue[0] != i:
        while True:
            for j in range(len(queue)):
                if queue[j] == i:
                    ans = j
                    break
            if j <= len(queue)/2:      #왼쪽
                l = queue.popleft()
                queue.append(l)
                count+=1
            else:                       #오른쪽
                l = queue.pop()
                queue.appendleft(l)
                count+=1 
            if queue[0] == i:
                queue.popleft()
                break

    elif queue[0] == i:
        queue.popleft()

print(count)

