import sys
from math import isqrt
input = sys.stdin.readline

dic = dict()
def find():
    cnt = 0
    for i in arr:
        j = (mi // i**2)*i**2
        if j < mi:
            j += i**2
        while j < ma+1:
            if j not in dic:
                cnt += 1
            dic[j] = 0
            j += i**2
    return cnt

mi,ma = map(int,input().split())
s, e = isqrt(mi), isqrt(ma)

prime = [i for i in range(e+1)]
prime[1] = 0
for i in range(2,isqrt(e+1)):
    for j in range(i**2,(e+1),i):
        prime[j] = 0
arr = []
for i in prime[2:]:
    if i:
        arr.append(i)

print(ma-mi+1-find())