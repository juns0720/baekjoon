import sys
input = sys.stdin.readline

a,b,c,d = map(int,input().split())
arr = list(map(int,input().split()))

for p in arr:
    cnt = 0
    d1 = p % (a + b)
    d2 = p % (c + d)

    if 1 <= d1 <= a:
        cnt += 1
    if 1 <= d2 <= c:
        cnt += 1
    print(cnt)