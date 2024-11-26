import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()

#최초 3명을 묶음
tmp = lst[2]-lst[0]

for i in range(4,n,2):
    tmp+=lst[i]-lst[i-1]
res = tmp


for i in range(2,n-1, 2):
    tmp += lst[i+2] - lst[i]
    tmp -= lst[i]   - lst[i-2]
    tmp += lst[i-1] - lst[i-2]
    tmp -= lst[i+2] - lst[i+1]
    res = min(tmp, res)

print(res)
