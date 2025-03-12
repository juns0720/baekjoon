import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

red = sorted(list(map(int,input().split())))
cards = list(map(int,input().split()))

parent = [i for i in range(m+1)]

def binary_search(target):
    s = -1
    e = len(red) -1
    
    while s + 1 < e:
        mid = (s+e) // 2
        if red[mid] > target:
            e = mid
        else:
            s = mid
    
    return e

def union(v1):
    a = parent[v1]
    parent[v1] += 1

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
    return parent[v1]


for card in cards:
    res_idx = binary_search(card)
    v1 = find(res_idx)
    print(red[v1])
    union(v1)
