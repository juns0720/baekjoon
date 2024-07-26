import sys
input = sys.stdin.readline

S,C = map(int,input().split())
onions = []
for i in range(S):
    onions.append(int(input()))
s = 0
e = max(onions)+1

while s+1 < e:
    mid = (s + e) // 2
    cnt = 0
    for onion in onions:
        cnt+= (onion // mid)
    if cnt >= C:
        s = mid
    else:
        e = mid

res = sum(onions)-C*s
print(res)