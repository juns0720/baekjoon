import sys
input = sys.stdin.readline

n = int(input())
ans = input().split()
dic = {ans[i]: i for i in range(n)}
stack = [dic[i] for i in input().split()]

total = n*(n-1)//2


cnt = 0
res = 0
tmp = [stack.pop()]
while stack:
  crnt = stack.pop()
  for prev in tmp:
    if crnt < prev:
      res+=1
  tmp.append(crnt)
print(str(res) +"/"+ str(total))