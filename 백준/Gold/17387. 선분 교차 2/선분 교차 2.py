import sys
input = sys.stdin.readline

p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))

def ccw(x1,y1,x2,y2,x3,y3):
    s = (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)
    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0

def check():
    ccw123 = ccw(p1[0],p1[1],p1[2],p1[3],p2[0],p2[1])
    ccw124 = ccw(p1[0],p1[1],p1[2],p1[3],p2[2],p2[3])
    ccw341 = ccw(p2[0],p2[1],p2[2],p2[3],p1[0],p1[1])
    ccw342 = ccw(p2[0],p2[1],p2[2],p2[3],p1[2],p1[3])
    l12 = ccw123 * ccw124
    l34 = ccw341 * ccw342
    if l12 == 0 and l34 == 0:
        if min(p1[0],p1[2]) <= max(p2[0],p2[2]) and min(p2[0],p2[2]) <= max(p1[0],p1[2]) and \
           min(p1[1],p1[3]) <= max(p2[1],p2[3]) and min(p2[1],p2[3]) <= max(p1[1],p1[3]):
            return 1
        
    elif l12 < 1 and  l34 < 1:
        return 1

    return 0

print(check())


