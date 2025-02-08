import sys
from itertools import product
input = sys.stdin.readline

N,K = map(int,input().split())
e = list(input().split())
arr = list(int(i) for i in str(N))
res = 0
for l in range(1,len(arr)+1):
  for i in product(e,repeat = l):
      num = int(''.join(i))
      if N >= num:
          res = max(res,num)

print(res)