import sys
from collections import deque
input = sys.stdin.readline
N,K,M = map(int,input().split())

arr = [i for i in range(1,N+1)]
num = K-1
print(arr.pop(num),end=' ')
cnt = 1
cntr = 0
while arr:
    if cnt == M:
        if cntr == M:
            cnt = 0
            cntr = 0
        else:
            num = num-K
            num%=len(arr)
            print(arr.pop(num),end=' ')
            cntr+=1
    else:
        num = (num+(K-1))%len(arr)
        print(arr.pop(num),end=' ')
        cnt+=1