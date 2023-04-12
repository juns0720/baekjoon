import sys
import collections
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))
l.sort()
lot = collections.Counter(l)
lot = sorted(lot.items(), key = lambda x: x[1],reverse = True)
print(round(sum(l)/N))
if N % 2 == 0:
    mid = N//2
    print((l[mid-1]+l[mid])//2)
else:
    print(l[N//2])
if N == 1:
    print(lot[0][0])
else:
    if lot[0][1] == lot[1][1]:
        print(lot[1][0])
    else:
        print(lot[0][0])
print(l[-1]-l[0])


