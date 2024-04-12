import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    a = list(map(int,input().split()))
    if a[0] == 0:
        if array:
            array.sort()
            print(array.pop())
        else:
            print(-1)
    else:
        for gift in range(1, a[0]+1):
            array.append(a[gift])

