import sys
input = sys.stdin.readline

arr = set()

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
 

for i in range(n):
    for j in range(n):
        arr.add(lst[i]+lst[j])

res = 0
for k in range(n-1,-1,-1):
    for z in range(n-1,-1,-1):
        if lst[k]-lst[z] in arr:
            res = max(lst[k],res)
print(res)