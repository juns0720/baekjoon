import sys
input = sys.stdin.readline

num = int(input())
l = []
temp = 0
for i in range(num):
   a,b = map(int,input().split())
   l.append([b,a])
l.sort()

for i in range(num):
   print(l[i][1],l[i][0])
