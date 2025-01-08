import sys
input = sys.stdin.readline

ry,rx = [],[]
for i in range(3):
    y,x = map(int,input().split())
    if y in ry:
        ry.remove(y)
    else:
        ry.append(y)

    if x in rx:
        rx.remove(x)
    else:
        rx.append(x)

print(*ry,*rx)