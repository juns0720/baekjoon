import sys
from itertools import combinations
input = sys.stdin.readline

N,K = map(int,input().split())
house = []

for i in range(N):
    x,y = map(int,input().split())
    house.append([x,y])

def cal_dist(x1,y1, x2,y2):
    return abs(x1-x2) + abs(y1-y2)
    
'''
1. 전체 집들중 대피소가 될 집 K개를 선택 한다.
2. 대피소가 아닌 집들 각각 대피소와의  거리를 계산한다.
 2.1 대피소와의 거리를 계산하고 가장 짧은 대피소와의 거리를 채택한다.
 2.2 채택된 거리를 최종 배열에 넣는다.
3. 채택된 거리들 중 가장 긴 거리를 선택한다.
'''

max_dist = 10**20

for shelter in list(combinations([i for i in range(N)],K)): # 대피소 K개를 선택
    not_shelter = []
    cur_dist = []

    # 대피소가 아닌 집들 확인
    for i in range(N):
        if i not in shelter:
            not_shelter.append(i)
 # 집 별 대피소와의 거리를 계산한다.
    for i in not_shelter:
        cur_house_dist = []
        for j in shelter:
        #집과 대피소와의 거리를 저장한다.
            cur_house_dist.append(cal_dist(house[i][0],house[i][1],house[j][0],house[j][1]))
        #가장 짧은 거리를 cur_dist에 넣는다.
        cur_dist.append(min(cur_house_dist))
    
    max_dist = min(max_dist, max(cur_dist))
print(max_dist)
