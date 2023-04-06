import sys
input = sys.stdin.readline
Sum = 1
for i in range(3):
    Sum *= int(input())
list1 =list(map(int,str(Sum)))
list1.sort()
cnt = 0
t = 0
for i in range(10):
    while True:
        if t >= len(list1):
            print(cnt)
            cnt = 0
            break
        elif list1[t] == i:
            cnt+=1
            t+=1
        else:
            print(cnt)
            cnt = 0
            break


