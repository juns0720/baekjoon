import sys
import heapq
input = sys.stdin.readline


N = int(input())
tlist = list(map(int,input().split()))

tlist.sort()
mid = ((N+1) // 2)
cnt = 0
tmp_list = tlist[:mid]

i = mid-1
while i >=0:
    if(tmp_list[i]== 1):
        i-=1
        continue
    tmp_list[i] //=2
    cnt+=1
print(cnt+1)