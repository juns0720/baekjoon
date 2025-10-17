import sys
input = sys.stdin.readline


dic = dict()
u,n = map(int,input().split())

for i in range(n):
    s,p = input().split()
    p = int(p)
    if p in dic:
        dic[p][1].append(s)
        dic[p][0] += 1
    else:
        dic[p] = [1,[s]]

lst = sorted(list(dic.items()), key = lambda x: (x[1][0],x[0]))

print(lst[0][1][1][0],lst[0][0])