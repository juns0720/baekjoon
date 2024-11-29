import sys
input = sys.stdin.readline

n = int(input())

lst = [int(input()) for _ in range(n)]

lst.sort()
max_len = -1
for i in range(n-2):
   if lst[i] + lst[i+1] > lst[i+2]:
      max_len = max(max_len, sum(lst[i:i+3]))
print(max_len)