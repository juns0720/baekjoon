import sys
input = sys.stdin.readline

'''
1. 한달에 최대 150만원까지 과금이 가능, 만원 단위로 과금할 수 있음.
2. 
'''

N = int(input())
limit = list(map(int,input().split()))

res = [0 for _ in range(N)]
cur_lev = list(input().strip())
lev = {'B': limit[0], 'S': limit[1], 'G': limit[2], 'P': limit[3], 'D': limit[3]}

for i in range(N):
    if i == 0:
        if cur_lev[i] == 'D':
            res[i] += lev[cur_lev[i]]
        else:
            res[i] += lev[cur_lev[i]]-1
    else:
        if cur_lev[i] == 'D':
            res[i] += lev[cur_lev[i]]
        else:
            res[i] += lev[cur_lev[i]]-res[i-1]-1
print(sum(res))
       
