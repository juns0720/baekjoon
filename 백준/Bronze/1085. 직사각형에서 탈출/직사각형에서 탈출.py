import math
x,y,w,h = map(int,input().split())
print(min(abs(w-x),x,abs(h-y),y))