import sys
input = sys.stdin.readline
import itertools

n,s = map(int, input().split())
cnt = 0
list =list(map(int,input().split()))
a = []
for i in range(1,n+1):
    for i in (itertools.combinations(list,i)):
        a.append(i)
for i in a:
    if sum(i) == s:
        cnt+=1
print(cnt)



 