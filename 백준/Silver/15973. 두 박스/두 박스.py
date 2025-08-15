import sys
input = sys.stdin.readline

px = []
py = []
for i in range(2):
    y1,x1,y2,x2 = map(int,input().split())
    py.append([y2,y1])
    px.append([x2,x1])
py.sort(key = lambda x: (-x[0],-x[1]))
px.sort(key = lambda x: (-x[0],-x[1]))

if py[0][1] == py[1][0] and px[0][1] == px[1][0]:
    print("POINT")
elif py[0][1] == py[1][0] or px[0][1] == px[1][0]:
    print("LINE")
elif not (py[0][1] <= py[1][0] <= py[0][0]) or not (px[0][1] <= px[1][0] <= px[0][0]):
    print("NULL")
else:
    print("FACE")