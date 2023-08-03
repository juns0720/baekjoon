import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
house = []
chicken = []
for i in range(1,N+1):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            house.append((i,j+1))
        elif temp[j] == 2:
            chicken.append((i,j+1))


Min = N*2*len(house)
for shop in combinations(chicken,M):
    temp = 0
    res = [N*2 for _ in range(len(house))]
    for j in range(M):
         for k in range(len(house)):
            res[k]=min(abs(house[k][0]-shop[j][0])+abs(house[k][1]-shop[j][1]),res[k])
    Min = min(sum(res),Min)
print(Min)
