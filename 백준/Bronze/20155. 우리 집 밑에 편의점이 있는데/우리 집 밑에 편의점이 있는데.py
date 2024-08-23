import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))
res = 0
for i in range(1,m+1):
    res =max(lst.count(i),res)
print(res)