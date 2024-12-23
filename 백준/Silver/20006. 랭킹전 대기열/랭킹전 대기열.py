import sys
input = sys.stdin.readline

p,m = map(int,input().split())

rooms = []

for _ in range(p):
    lev, name = input().split()
    lev = int(lev)
    enter = False
    for room in rooms:
        if len(room) == m or room[0][0] - 10 > lev or lev > room[0][0] + 10:
            continue
        room.append((lev,name))
        enter = True
        break
    if not enter:
        rooms.append([(lev,name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for p in sorted(room, key = lambda x: x[1]):
        print(p[0],p[1])
