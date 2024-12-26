import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
    return parent[v1]

def union(v1,v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1
cnt = 0
airplanes = []
for i in range(P):
    airplanes.append(int(input()))
for airplane in airplanes:
    prnt = find(airplane)
    if prnt == 0:
        break
    union(prnt-1, prnt)
    cnt+=1
print(cnt)
    
        

