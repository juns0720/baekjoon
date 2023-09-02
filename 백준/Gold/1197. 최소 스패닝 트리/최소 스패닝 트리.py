import sys
input = sys.stdin.readline

V,E = map(int,input().split())
parent = [i for i in range(V+1)]
def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

arr = []
sum = 0
for i in range(E):
    a,b,c = map(int,input().split())
    arr.append([min(a,b),max(a,b),c])
arr.sort(key = lambda x:x[2])


for i in arr:
    if find(i[0]) != find(i[1]):
        union(i[0],i[1])
        sum+=i[2]
print(sum)