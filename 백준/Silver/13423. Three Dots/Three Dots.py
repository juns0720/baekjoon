import sys
input = sys.stdin.readline

def binary_search(s,e,target):
    
    while s+1 < e:
        mid = (s+e) // 2
        if dots[mid] < target:
            e = mid
        else:
            s = mid
    if dots[s] == target:
        return 1
    return 0

for tc in range(int(input())):
    n = int(input())
    dots = sorted(list(map(int,input().split())))
    dots.reverse()
    res = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            gap = dots[i]-dots[j]
            target = dots[j]-gap
            res += binary_search(j+1,n,dots[j]-gap)
    print(res)