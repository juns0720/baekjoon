import sys
input = sys.stdin.readline



def binary_search(target):
    s = 0
    e = len(B)
    while s + 1 < e:
        mid = (s + e) // 2
        if B[mid] <= target:
            s = mid
        else:
            e = mid
    if e == len(B):
        return B[s]
    else:
        if abs(B[s]-target) <= abs(B[e]-target):
            return B[s]
        else:
            return B[e]
    



for tc in range(int(input())):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = sorted(list(map(int,input().split())))
    res = 0
    for num in A:
        res += binary_search(num)
    print(res)