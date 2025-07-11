import sys
input = sys.stdin.readline

n = int(input())

res = 0
dic = dict()
s = 0
for i in list(map(int,input().split())):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    if i == 0 or i > n:
        res = -1

for k,v in dic.items():

    if k == v:
        res = max(k,res)
print(res)