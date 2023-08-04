import sys
from collections import deque
input = sys.stdin.readline
def CW_Right(n):     #시계방향 오른쪽 톱니 
    if n < 4:
        # print(n+1,"번째톱니 변경전",gear[n])
        num = gear[n][2]
        tmp = gear[n].popleft()
        gear[n].append(tmp)
        # print(n+1,"번째톱니 변경후",gear[n])
        if n != 3 and num != gear[n+1][6]:
            CCW_Right(n+1)

def CCW_Right(n):    #반시계방향 오른쪽 톱니 
    if n < 4:
        # print(n+1,"번째톱니 변경전",gear[n])
        num = gear[n][2]
        tmp = gear[n].pop()
        gear[n].appendleft(tmp)
        # print(n+1,"번째톱니 변경후",gear[n])
        if n != 3 and num != gear[n+1][6]:
            CW_Right(n+1)

def CW_Left(n):      #시계방향 왼쪽 톱니 
    if n > -1:
        # print(n+1,"번째톱니 변경후",gear[n])
        num = gear[n][6]
        tmp = gear[n].popleft()
        gear[n].append(tmp)
        # print(n+1,"번째톱니 변경후",gear[n])
        if n != 0 and num != gear[n-1][2]:
            CCW_Left(n-1)

def CCW_Left(n):     #반시계방향 왼쪽 톱니
     if n > -1:
        # print(n+1,"번째톱니 변경후",gear[n])
        num = gear[n][6]
        tmp = gear[n].pop()
        gear[n].appendleft(tmp)
        # print(n+1,"번째톱니 변경후",gear[n])
        if n != 0 and num != gear[n-1][2]:
            CW_Left(n-1)

def CCW_Left_f(now_num,n):     #반시계방향 왼쪽 톱니
    if n > 0 and now_num != gear[n-1][2]:
        CW_Left(n-1)

def CW_Left_f(now_num,n):      #시계방향 왼쪽 톱니 
        if n > 0 and now_num != gear[n-1][2]:
            CCW_Left(n-1)
def move(n,vec):
    if vec == 1:    #시계방향이면
        if n == 0:
            CCW_Right(n)
        elif n == 3:
            CCW_Left(n)
        else:
            now_num = gear[n][6]
            CCW_Right(n)
            CCW_Left_f(now_num,n)
    elif vec == -1:
        if n == 0:
            CW_Right(n)
        elif n == 3:
            CW_Left(n)
        else:
            now_num = gear[n][6]
            CW_Right(n)
            CW_Left_f(now_num,n)

gear = deque([deque(list(input().strip())) for _ in range(4)])
rotations = []

for i in range(int(input())):
    rotations.append(list(map(int,input().split())))

for (n,vec) in rotations:
    move(n-1,vec)
print(int(gear[0][0])*1 + int(gear[1][0])*2 + int(gear[2][0])*4 + int(gear[3][0])*8)