import sys
import math
input = sys.stdin.readline

def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)
while True:
    try:
        inp = list(input().split())
        arr = list(inp[0])
        n = int(inp[1])
    except:
        exit()
    print(*inp,'=',end = ' ')
    res = []
    cnt = fac(len(arr))
    while arr:
        gap = cnt // len(arr)
        curr_gap = math.ceil(n / gap)
        arr.sort()
        if curr_gap-1 > len(arr)-1:
            res = ["No permutation"]
            break
        res.append(arr[curr_gap-1])
        arr.pop(curr_gap-1)
        cnt = gap
        n = gap - (gap*curr_gap - n)

    print(''.join(res))
    