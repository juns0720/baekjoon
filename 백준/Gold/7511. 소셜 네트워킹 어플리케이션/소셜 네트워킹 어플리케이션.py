import sys
input = sys.stdin.readline

def union(v1, v2):

   if v1 > v2:
      parent[v1] = v2
   else:
      parent[v2] = v1

def find(v):
   if parent[v] != v:
      parent[v] = find(parent[v])

   return parent[v]

T = int(input())
for tc in range(1,T+1):
   print(f"Scenario {tc}:")
   n = int(input())
   parent = [i for i in range(n+1)]

   for _ in range(int(input())):
      a,b = map(int,input().split())
      a,b = find(a), find(b)
      if a != b:
         union(a, b)
   
   for _ in range(int(input())):
      a,b = map(int,input().split())
      print(int(find(a) == find(b)))
   if tc == T:
      continue
   print()