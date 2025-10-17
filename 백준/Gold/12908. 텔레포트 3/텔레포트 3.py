import sys
input = sys.stdin.readline

xs, ys = map(int,input().split())
xe, ye = map(int,input().split())

def cal_sec(x1,y1,x2,y2):
   return abs(x2-x1) + abs(y2-y1)

tp = dict()
pos = []
for i in range(3):
   x1,y1,x2,y2 = map(int,input().split())
   if cal_sec(x1,y1,x2,y2) > 10:
      tp[(x1,y1,x2,y2)] = 10
      tp[(x2,y2,x1,y1)] = 10
      pos.append((x1,y1))
      pos.append((x2,y2))

min_sec = sys.maxsize
pos.sort(key = lambda x: (x[0], x[1]))
visited = dict()

def find(x, y, sec, idx):
   global min_sec
   
   min_sec = min(min_sec, sec + cal_sec(x,y,xe,ye))
   
   for i in range(len(pos)):
      if i == idx:
         continue
      nx,ny = pos[i]

      if (nx,ny) in visited:
         continue

      if (x,y,nx,ny) in tp:
         n_sec = 10
      else:
         n_sec = cal_sec(x,y,nx,ny)
      visited[nx,ny] = 1
      find(nx,ny,sec+n_sec,i)
      visited.pop((nx,ny))

find(xs,ys,0,-1)

print(min_sec)