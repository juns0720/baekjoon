import sys
input = sys.stdin.readline

n = int(input())

dic = dict()

for i in range(n):
    s = input().strip().split('.')
    if s[1] in dic:
        dic[s[1]] += 1
    else:
        dic[s[1]] = 1

res = sorted(list(dic.items()), key = lambda x: x[0])
for i in res:
    print(*i)