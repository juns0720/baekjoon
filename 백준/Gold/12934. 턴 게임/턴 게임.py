import sys
x,y = map(int,input().split())

MAX_SIZE = (10**12)*2
max_count = 0

num = 0
make = 0 
for i in range(1, MAX_SIZE+1):
    if num == (x + y):
        make = 1
        break
    if num + i > MAX_SIZE:
        break
    max_count += 1
    num += i
if not make:
    print(-1)
else:
    res = 0
    cnt = 0
    for i in range(max_count, 0,-1):
        if res + i <= x:
            res += i
            cnt += 1
        if res == x:
            break
    print(cnt)