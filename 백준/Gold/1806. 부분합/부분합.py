import sys
import math
input = sys.stdin.readline
'''
1. S보다 작으면 e+=1
2. S보다 크면 e-=1
    2.1 최솟값 갱신
'''

N,S = map(int,input().split())
lst = list(map(int,input().split()))
s,e = 0,0
res = 100001
sum_num = lst[0]
while True:   
    if sum_num < S:
        e+=1
        if e == N:
            break
        sum_num += lst[e]
    else:
        sum_num -= lst[s]
        res = min(res,e-s+1)
        s+=1
print(0 if res == 100001 else res)