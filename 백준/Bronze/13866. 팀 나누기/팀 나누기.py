import sys
from itertools import combinations

lst = list(map(int,input().split()))

res = 10**9
for teamA in combinations(range(4),2):
    teamB = []
    for h in range(4):
        if h not in teamA:
            teamB.append(h)
    sumA,sumB = 0,0
    for i in range(2):
        sumA += lst[teamA[i]]
        sumB += lst[teamB[i]]
    res = min(res, abs(sumA-sumB))
print(res)