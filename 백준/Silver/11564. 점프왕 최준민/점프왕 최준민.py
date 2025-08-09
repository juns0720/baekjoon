import sys
input = sys.stdin.readline

k,a,b = map(int,input().split())
if a*b < 0:
    cnt = 1
    a,b = abs(a), abs(b)
    cnt += (a//k + b//k)
else:
    a,b = min(abs(a), abs(b)),max(abs(a), abs(b))
    cnt = 0
    cnt += ((b//k) - ((a+k)//k) + 1)
    if a % k == 0:
        cnt += 1
print(cnt)

