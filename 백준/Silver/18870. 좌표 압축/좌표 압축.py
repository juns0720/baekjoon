import sys
import copy
input = sys.stdin.readline

n = int(input())
pos = list(map(int,input().split()))
pos_copy = copy.deepcopy(pos)
pos = list(set(pos))
pos_d =dict()

pos.sort()
num = 0
for i in pos:
    pos_d[i] = num
    num+=1
for i in pos_copy:
    print(pos_d[i],end=' ')
