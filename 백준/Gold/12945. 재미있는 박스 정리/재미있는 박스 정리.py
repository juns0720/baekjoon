import sys
input = sys.stdin.readline

n = int(input())
box = sorted([int(input()) for _ in range(n)])
s = 0
e = n // 2
res = 0
while s < n // 2 and e < n:
    if box[e] < box[s]*2:
        e += 1
    else:
        e +=1
        s +=1
        res += 1

print(n-res)