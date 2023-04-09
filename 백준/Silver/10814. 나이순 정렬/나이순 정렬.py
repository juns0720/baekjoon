import sys
N = int(input())
l = []
for i in range(N):
    l.append(list(input().split()))
l.sort(key = lambda x: int(x[0]))

for i in range(N):
    print(l[i][0], l[i][1])