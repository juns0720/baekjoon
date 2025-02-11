import sys
input = sys.stdin.readline

n,m = map(int,input().split())
titles = []


def binary_search(power):
    s = 0
    e = len(titles)
    res = 0
    while s <= e:
        mid = (s + e) // 2
        if  power <= titles[mid][1]:
            e = mid - 1
            res = mid
        else:
            s = mid + 1
    print(titles[res][0])

for i in range(n):
    a,b = list(input().strip().split())
    titles.append([a,int(b)])

for i in range(m):
    power = int(input())
    binary_search(power)