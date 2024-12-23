import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    s1 = input().strip().split(",")
    pages = set()
    for rng in s1:
        tmp = rng.split("-")
        if len(tmp) == 1:
            if int(tmp[0]) <= n:
                pages.add(int(tmp[0]))
            continue
        l,r = int(tmp[0]),int(tmp[1])
        if l > r:
            continue
        elif r > n:
            r = n
        for page in range(l,r+1):
            pages.add(page)
    print(len(pages))