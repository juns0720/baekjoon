import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
people = [0 for _ in range(n)]

for i in range(n):
    card = list(map(int,input().split()))
    max_num = 0
    for j in permutations(card,3):
        max_num = max(max_num, sum(j)%10)
    people[i] = (i,max_num)
people.sort(key = lambda x : [-x[1], -x[0]])
print(people[0][0]+1)
