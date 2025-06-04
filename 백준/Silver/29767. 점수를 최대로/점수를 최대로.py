import sys
n,k = map(int,input().split())
arr = list(map(int,input().split()))

prefix = [0 for i in range(n)]

prefix[0]= arr[0]

for i in range(1,n):
    prefix[i] = prefix[i-1] + arr[i]
prefix.sort(key = lambda x : -x)
res = 0

for i in range(k):
    res += prefix[i]
print(res)