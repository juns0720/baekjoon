from collections import deque
import sys
input = sys.stdin.readline

def bfs(n,m):
  operation = ["D","S","L","R"]
  
  visited = {}
  visited[n] = 1

  q = deque()
  q.append([n,[]])

  while q:
    now, oper = q.popleft()
    if now == m:
      return oper
    
    d = (now*2)%(10**4)
    s = now-1 if now != 0 else 9999
    l = now%1000*10 + now//1000
    r = now%10*1000 + now//10
    res = [d,s,l,r]

    for i in range(4):
      if not visited.get(res[i]):
        q.append((res[i], oper + [operation[i]]))
        visited[res[i]] = 1

test_case = int(input())
for _ in range(test_case):
  n,m = map(int, input().split())
  print(''.join(bfs(n,m)))