import sys
input = sys.stdin.readline

N,B,H,W = map(int,input().split())

min_cost = sys.maxsize
for i in range(H):
    cost = int(input())
    total_cost = cost*N
    max_stay = max(list(map(int,input().split())))
    if max_stay >= N and total_cost <= B:
        min_cost = min(min_cost,total_cost)
print("stay home") if min_cost == sys.maxsize else print(min_cost)