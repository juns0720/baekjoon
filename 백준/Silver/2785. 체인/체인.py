import sys
from collections import deque
input = sys.stdin.readline

'''짧은 고리를 끊어서 긴 고리끼리 묶는다.'''


N = int(input())
chains = list(map(int,input().split()))

chains.sort()
start = 0
end = N-1
cnt = 0
while True:
    if start == end:
        break
    if chains[start] > 0:
        chains[start]-=1
        end-=1
        cnt+=1
    else:
        start+=1
print(cnt)