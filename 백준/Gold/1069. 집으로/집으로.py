import sys
from math import sqrt
input = sys.stdin.readline

x,y,d,t = map(int,input().split())
md = sqrt(x**2 + y**2)
if d <= t:
    print(md)
    exit()
res = 0.0
while True:
    if md <= 2*d:
        break
    md -= d
    res += t
res += min(abs(md-d)+t, 2*t, md)
print(res)