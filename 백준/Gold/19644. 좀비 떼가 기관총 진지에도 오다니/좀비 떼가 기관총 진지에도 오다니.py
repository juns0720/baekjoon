import sys
from math import ceil
input = sys.stdin.readline

L = int(input())
Ml, Mk = map(int,input().split())
C = int(input())
road = [int(input()) for _ in range(L)]

damage = [0 for _ in range(L)]

for i in range(Ml):
    if i > L-1:
        break
    damage[i] = Mk*(i+1)
for i in range(Ml,L):
    damage[i] = damage[i-1]


cnt = 0
val = Ml
if Ml > 1:
    val -= 1
for i in range(L):
    if damage[i] - Mk*(ceil(cnt/(val))) < road[i]:
        if C > 0:
            C -= 1
            cnt += Ml-1
        else:
            print("NO")
            exit()
    else:
        if cnt > 0:
            cnt -= 1
print("YES")
