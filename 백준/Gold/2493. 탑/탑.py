import sys
input = sys.stdin.readline
N =int(input())
arr =list(map(int,input().split()))
res = dict()
l1 = []
l1.append([1,arr[0]])
for i in arr :
    res[i] = 0
for i in range(1,len(arr)):
    while l1:
        if l1[-1][1] < arr[i]:
            l1.pop()
        else:
            res[arr[i]] = l1[-1][0]
            l1.append([i+1,arr[i]])
            break
    if not l1:
        l1.append([i+1,arr[i]])

for item in res.values():
    print(item,end=' ')