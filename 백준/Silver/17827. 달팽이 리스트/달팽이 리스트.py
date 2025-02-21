import sys
input = sys.stdin.readline

N,M,V = map(int,input().split())
graph = list(map(int,input().split()))
cycle = N+1 - V
for i in range(M):
    seq = int(input())
    if seq < N-1:
        idx = seq
    else:
        idx = ((seq - (N-1)) % cycle)
        if idx == 0:
            idx = N-1
        else:
            idx += 1
    print(graph[idx])
