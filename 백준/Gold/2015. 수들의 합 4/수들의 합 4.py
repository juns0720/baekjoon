import sys
input = sys.stdin.readline
n,k = map(int,input().split())
seq = list(map(int,input().split()))
prefix = [0 for _ in range(n+1)]

dic = {0:1}
tmp = 0
res = 0
for i in seq:
    tmp += i
    if tmp - k in dic:
        res += dic[tmp-k]
    if tmp not in dic:
        dic[tmp] = 1
    else:
        dic[tmp] += 1       
        
print(res)