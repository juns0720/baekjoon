import sys
import math
input = sys.stdin.readline

N,Q = map(int,input().split())
MAX = math.ceil(math.log2(N))
tree = [0 for _ in range(1 << (MAX + 1))]

def update(node, start, end):
    if start <= p <= end:
        tree[node] += q
        if start != end:
            mid = (start + end) // 2
            update(node*2, start, mid)
            update((node*2)+1, mid + 1, end)

def cal(node, start, end):
    if q < start or p > end:
        return 0
    if p <= start and q >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return cal(node*2, start, mid) + cal(node*2+1, mid + 1, end)

for _ in range(Q):
    command,p,q = map(int,input().split())
    if command == 1:
        p -= 1
        update(1, 0, N-1)
    else:
        p -= 1
        q -= 1
        print(cal(1,0,N-1))
