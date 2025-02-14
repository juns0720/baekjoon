import sys
input = sys.stdin.readline

n = int(input())

edge = dict()
graph = [[] for _ in range(n+1)]

for i in range(1,n):
    v1,v2 = map(int,input().split())
    edge[i] = (v1,v2)
    graph[v1].append(v2)
    graph[v2].append(v1)

for q in range(int(input())):
    t,k = map(int,input().split())

    if t == 1:
        cnt = n-1 - len(graph[k])
        if cnt == n-2:
            print("no")
        else:
            print("yes")
    elif t == 2:
        print("yes")