import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque([i for i in range(1,n+1)])

cnt = 0
while len(arr) > 1:
    num = arr.popleft()
    cnt = (cnt + 1) % 2
    if cnt == 0:
        arr.append(num)
    else:
        print(num, end = ' ')
print(arr[0])