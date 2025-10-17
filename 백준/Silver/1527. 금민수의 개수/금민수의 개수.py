import sys

input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 0

def find(num):
   global cnt
   if num and a <= int(num) <= b:
      cnt += 1
   if num and int(num) > b:
      return
   for i in ['4','7']:
      find(num + i)

find('')
print(cnt)