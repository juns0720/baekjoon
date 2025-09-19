import sys
from itertools import permutations 
input = sys.stdin.readline

s = list(input().strip())

def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)


res = 0
dic = dict()
if len(s) == len(set(s)):
    print(fac(len(s)))
    exit()

for arr in set(permutations(s)):
    if hash(arr) in dic:
        continue
    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            break
    else:
        dic[hash(arr)] = 1
        res += 1

print(res)