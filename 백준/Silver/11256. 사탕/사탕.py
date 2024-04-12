import sys
import math
input = sys.stdin.readline

for tc in range(int(input())):
    totalCandy, totalBox = map(int,input().split())
    boxes = []
    for box in range(totalBox):
        height, width = map(int,input().split())
        boxes.append(height * width)
    boxes.sort(reverse = True)
    cnt = 0
    for box in boxes:
        if(totalCandy <= 0):
            break
        totalCandy-= box
        cnt+=1

    print(cnt)