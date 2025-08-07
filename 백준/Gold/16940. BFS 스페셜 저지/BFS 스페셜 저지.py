import sys
input = sys.stdin.readline
n = int(input())
graph = [set() for _ in range(n+1)]

for i in range(n-1):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
seq = list(map(int,input().split()))
if seq[0] != 1:
    print(0)
    exit()
s = 0
e = 1

while s < e and e < n:
    if seq[e] in graph[seq[s]]:
        e += 1
    else:
        s += 1
if s == n-1 or s == e:
    print(0)
else:
    print(1)