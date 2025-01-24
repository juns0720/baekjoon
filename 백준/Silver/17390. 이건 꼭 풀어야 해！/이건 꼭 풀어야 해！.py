import sys

N,Q = map(int,input().split())
seq = sorted(list(map(int,input().split())))

prefix = [0 for _ in range(N)]
prefix[0] = seq[0]
for i in range(1,N):
    prefix[i] = prefix[i-1]+seq[i]
    
order = []
for i in range(Q):
    s,e = map(int,input().split())
    order.append((s-1,e-1))

for s,e in order:
    if s == 0:
        res = prefix[e]
    else:
        res = prefix[e]-prefix[s-1]
    print(res)