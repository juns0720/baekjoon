import sys
input = sys.stdin.readline

N = int(input())
num = [0 for _ in range(N+1)]
res = set()
same = set()
tmp = []
for i in range(1,N+1):
    num[i] = int(input())

def DFS(n,start):
    visited[n] = 1
    tmp.append(n)
    if num[n] == start:
        for i in tmp:
            res.add(i)
    if not visited[num[n]]:
        DFS(num[n],start)

for i in range(1,N+1):
    if i == num[i]:
        res.add(i)
    else:
        visited = [0 for _ in range(N+1)]
        DFS(i,i)
        tmp.clear()
res = list(res)
res.sort()
print(len(res))
for i in res:
    print(i)