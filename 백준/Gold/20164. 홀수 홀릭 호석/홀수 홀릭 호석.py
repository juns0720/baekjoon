
"""
1. 한 자리 수
 - 바로 종료

2. 두 자리 수
 - 2개로 나눠서 합을 구하여 새로운 수로 생각.

3. 세 자리 이상의 수
 - 임의의 위치에서 끊어서 3개의 수로 분할하고 3개를 더한 값을 새로운 수로 생각.

분할 포인트 3개 잡기
"""
def convert(n, p1,p2):
    return list(str(int(''.join(n[:p1])) + int(''.join(n[p1:p2])) + int(''.join(n[p2:]))))

def recursion(n, cnt):
    for i in n:
        if int(i) % 2 == 1:
            cnt+=1
    if len(n) == 1:
        res[0] = min(res[0], cnt)
        res[1] = max(res[1], cnt)
        return
    elif len(n) == 2:
        next_arr = list(str(int(n[0]) + int(n[1])))
        recursion(next_arr, cnt)
    else:
        for p in list(combinations([i for i in range(1, len(n))], 2)):
            next_arr = convert(n, p[0], p[1])
            recursion(next_arr, cnt)
    
import sys
from itertools import combinations
input = sys.stdin.readline

N = list(input().strip())
res = [10**9,0]
recursion(N, 0)
print(res[0],res[1])