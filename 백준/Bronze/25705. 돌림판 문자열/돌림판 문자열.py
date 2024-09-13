import sys
input = sys.stdin.readline

N = int(input())
s1 = (input().strip())
M = int(input())
s2 = list(input().strip())

s1*=(M+1)
idx = 0
cnt = 0
for i in range(len(s1)):
   if idx == len(s2):
      print(i)
      exit()
   if s1[i] == s2[idx]:
      idx+=1
print(-1)