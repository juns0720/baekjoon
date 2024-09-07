import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

prev = arr[0]
lst = []
for i in range(1, N):
    if prev != arr[i]:
        lst.append(i)
        prev = arr[i]
lst = [0] + lst + [N]
for i in range(1, len(lst)):
    for _ in range(lst[i-1], lst[i]):
        print(-1,end=' ') if i == len(lst)-1 else print(lst[i]+1,end=' ')