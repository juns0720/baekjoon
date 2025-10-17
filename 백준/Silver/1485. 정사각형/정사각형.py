import sys
import math
input = sys.stdin.readline


def cal(p1,p2):
    return math.sqrt(abs(p1[1]-p2[1])**2 + abs(p1[0]-p2[0])**2)
for tc in range(int(input())):
    pos = [list(map(int,input().split())) for _ in range(4)]
    dic = dict()
    for i in range(4):
        for j in range(i+1,4):
            l = cal(pos[i],pos[j])
            if l in dic:
                dic[l] += 1
            else:
                dic[l] = 1
    
    length = sorted(list(dic.items()),key = lambda x: -x[1])
    
    if len(length) == 2 and length[0][1] == 4:
        print(1)
    else:
        print(0)
