import sys
input = sys.stdin.readline

ma,mb = map(int,input().split())
ta,tb = map(int,input().split())
pa,pb = map(int,input().split())

d1 = min(ma,tb,pa)
d2 = min(mb,ta,pb)
if d1 + d2 == 0:
    print(0)
elif d1+d2 == d1 or d1+d2 == d2:
    print(1)
else:
    m = min(d1,d2)
    if d1 == d2:
        print(2*m)
    else:
        print(2*m+1)