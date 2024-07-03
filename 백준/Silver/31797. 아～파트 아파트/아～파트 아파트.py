import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
for i in range(1,m+1):
    s,e = map(int,input().split())
    lst.append([i,s])
    lst.append([i,e])
lst = sorted(lst,key = lambda x: x[1])
print(lst[n%(m*2)-1][0])