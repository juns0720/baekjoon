import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

arr = [list(input().strip()) for _ in range(n)]
k = int(input())

def base10(s):
    n = len(s)
    res = 0
    for i in range(n):
        cur_s = s[i]
        if s[i] in dic:
            cur_s = dic[s[i]]

        if 47 < ord(cur_s) < 58:
            res += (int(cur_s))*36**(n-1-i)
        else:
            res += (ord(cur_s)-55)*36**(n-1-i)

    return res

def base36(n):
    tmp = []
    cnt = 0
    if n == 0:
        tmp.append(0)
        cnt = 1
    while n > 0:
        m = n % 36
        n //= 36
        tmp.append(m)
        cnt += 1
    tmp.reverse()
    res = []

    for i in range(cnt):
        if  -1 < tmp[i] < 10:
            res.append(str(tmp[i]))
        else:
            res.append(chr(tmp[i] + 55))

    return ''.join(res)


weight = {base36(i):0 for i in range(36)}
dic = {}
for s1 in arr: 
    n = len(s1)
    for i in range(n):
        weight[s1[i]] += ((base10('Z')-base10(s1[i]))*36**(n-i))
weight = sorted(weight.items(), key = lambda x: -x[1])

for i in range(k):
    dic[weight[i][0]] = 'Z'

res = 0
for s in arr:
    res += base10(s)
print(base36(res))