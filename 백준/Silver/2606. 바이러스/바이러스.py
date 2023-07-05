import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(t,count):
	node = t
	visited[node] = True
	count+=1
	
	for i in graph[node]:
		if visited[i] == False:
			count = DFS(i,count)
	return count
print(DFS(1,-1))
