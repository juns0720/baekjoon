import sys
input = sys.stdin.readline
n = int(input())
dic = dict()

for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

arr = sorted(dic.items(),key = lambda x: x[0])
prev, h = arr[0]
w = 1
res = 0
for k,v in arr[1:]:
    if k-1 == prev:
        w += 1
        h = max(v,h)
    else:
        res += w*h
        w = 1
        h = v
    prev = k
res += w*h

print(res)